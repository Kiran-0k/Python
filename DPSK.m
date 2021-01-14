clc; close all;

N = 1e6;
BER = 0:2:16;
M = 2;

refArray = [1+0i, 0+1i, -1+0i, 0-1i];

symErrSimulated = zeros(2,length(BER));
k = log2(M);
BERs = BER + 10*log10(k);

data = 2*ceil(M.*rand(N,1))-1;
data_diff = filter(1,[1,-1], data);
s = refArray(mod(data_diff, 2*M)+1);

i = 1;
for x = BERs
    noiseVariance = 1/(10.^(x/10));
    noiseSigma = sqrt(noiseVariance/2);
    noise = noiseSigma*(randn(1,N)+1i*randn(1,N));
    received = s + noise;
    
    estPhase = angle(received);
    est_diffPhase = filter([1,-1],1,estPhase)*M/pi;
    y = mod(2*floor(est_diffPhase/2)+1,2*M);
    symErrSimulated(1,i) = sum(y~=data')/(N*k);
    i = i+1;
end

BERn = 10.^(BERs/10);
BERn = 10.^(BER/10);
symErrTheory = 0.5*exp(-BERn);

figure
semilogy(BER,symErrTheory,'b','linewidth',1.5);hold on;
semilogy(BER,symErrSimulated,'r*','linewidth',1.5);hold on;
legend({'Theory','Simulated'});grid on;
xlabel('Eb/N0(dB)');ylabel('Bit Error Rate(Pb)');
title('Simulation BER vs Theoretical BER for Binary DPSK');
