function hubble_matlab_audit(source_root)
% Independently audit saved Banik MAT objects in MATLAB R2020a/b.
% Usage (from this repo): addpath('verification'); hubble_matlab_audit('/path/to/hubFrct_2021')
% Source: https://github.com/JQIamo/hubFrct_2021 at commit
% 88c8a87aed5961f589db66a7e7e4e97f161ad51c. No data are modified.
% NOTE: This script has not been run in MATLAB in this workspace. It is not
% a replication of the authors' global fit and does not refit fi or Qi.
%
% To independently check source identity, verify all MAT-file SHA-256 hashes
% against verification/hubble_data_inventory.json before running MATLAB.

assert(isfolder(source_root), 'Source root does not exist');
addpath(genpath(fullfile(source_root, 'source')));
branches = {'expansions', 'contractions'};
tol_time = 1e-9;
max_profile_err = 0;
max_reference_err = 0;
count_dynamic = 0;
count_static = 0;
reused_endpoint_count = 0;

for ib = 1:numel(branches)
    branch = branches{ib};
    files = dir(fullfile(source_root, 'data', branch, 'PhnRuns_*.mat'));
    assert(~isempty(files), 'No MAT files in %s', branch);
    for k = 1:numel(files)
        file_path = fullfile(files(k).folder, files(k).name);
        S = load(file_path, 'A', 'Runs', 'time', 'n1Ds');
        A = S.A;
        t = A.EvTime(:);
        times = S.time(:);
        runs = S.Runs(:);
        phmask = ismember(runs, A.RunNos_phnEv(:));
        raw = S.n1Ds;
        assert(size(raw, 2) == numel(runs) && numel(times) == numel(runs));
        means = zeros(size(raw, 1), numel(t));
        for j = 1:numel(t)
            shot = phmask & abs(times - t(j)) <= tol_time;
            assert(nnz(shot) >= 2, 'Insufficient phonon repetitions');
            means(:, j) = mean(raw(:, shot), 2);
        end
        if isempty(A.RunNos_ring_I)
            init = mean(means(:, t <= A.t_phn1), 2);
        else
            init = mean(raw(:, ismember(runs, A.RunNos_ring_I(:))), 2);
        end
        max_reference_err = max(max_reference_err, max(abs(init - A.n1D_ringI_avg(:))));
        if strcmp(A.dataRingType, 'All')
            count_dynamic = count_dynamic + 1;
            assert(isempty(A.RunNos_ring_F), 'Unexpected explicit final reference');
            tend = A.t_phn1 + A.t_exp;
            final = mean(means(:, t >= tend), 2);
            max_reference_err = max(max_reference_err, max(abs(final - A.n1D_ringF_avg(:))));
            exp_times = A.n1D_ringExpTimes(:);
            ramp = zeros(size(raw,1), numel(exp_times));
            rm = ismember(runs, A.RunNos_ring_Exp(:));
            for j = 1:numel(exp_times)
                sel = rm & abs(times - exp_times(j)) <= tol_time;
                assert(nnz(sel) >= 2, 'Insufficient ramp reference repetitions');
                ramp(:, j) = mean(raw(:, sel), 2);
            end
            ramp_err = abs(ramp - A.n1D_ringExp_avg);
            max_reference_err = max(max_reference_err, max(ramp_err(:)));
        elseif strcmp(A.dataRingType, 'Initial')
            count_static = count_static + 1;
            fprintf('STATIC %s %s radius=%.8f fi=%.8f Qi=%.8f\n', ...
                branch, files(k).name, mean(A.MeanRad_avg(:)), A.fi, A.Qi);
            tend = A.t_phn1 + A.t_exp;
        else
            error('Unexpected dataRingType: %s', A.dataRingType);
        end
        previous = [];
        for j = 1:numel(t)
            % Mirror the author's exact comparisons and persistent reference.
            if t(j) <= A.t_phn1
                previous = init;
            elseif t(j) >= tend
                previous = final;
            else
                matches = find(exp_times == t(j));
                assert(numel(matches) <= 1);
                if ~isempty(matches)
                    previous = ramp(:, matches(1));
                elseif abs(t(j) - tend) <= tol_time
                    reused_endpoint_count = reused_endpoint_count + 1;
                    fprintf('REUSED_END %s %s\n', branch, files(k).name);
                else
                    error('Unmatched non-endpoint ramp reference');
                end
            end
            assert(~isempty(previous) && abs(sum(previous)) > 1e-8);
            predicted = means(:, j) - previous * sum(means(:, j)) / sum(previous);
            max_profile_err = max(max_profile_err, max(abs(predicted - A.n1D_phnEv_avg(:, j))));
        end
    end
end
fprintf('dynamic=%d static_files=%d reused_endpoints=%d max_ref_error=%.12g max_profile_error=%.12g\n', ...
    count_dynamic, count_static, reused_endpoint_count, max_reference_err, max_profile_err);
assert(count_dynamic == 28 && count_static == 14, 'Unexpected data classification');
assert(max_reference_err < 1e-7 && max_profile_err < 1e-7, 'Profile mismatch');
% Expected endpoint count is seven according to the independent Python audit;
% leave it as an output rather than assuming MATLAB must reproduce it.
end
