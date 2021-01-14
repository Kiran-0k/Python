clc; close all;

n = 4;
L = 2^n;

numSamples = 12;

x = 0:2*pi/numSamples:4*pi;

s= 8*sin(x);
subplot(3,1,1)
plot(s);
title('Analog S/L');
subplot(3,1,2)
stem(s);grid on;
title('Sampled S/L');

vmax = 8;
vmin = -vmax;
delta = (vmax-vmin)/L;
part = vmin:delta:vmax;
code = vmin-(delta/2):delta:vmax+(delta/2);
[ind, q] = quantiz(s,part,code);
subplot(3,1,3)
stem(q);grid on;
title('Quantized');

l1 = length(ind);
l2 = length(q);

code = dec2bin(ind);
k = 1;

for i=1:l1
    for j=1:n
        coded(k)=str2num(code(i,j));
        j = j+1;
        k = k+1;
    end
    i = i+1;
end

figure
subplot(2,1,1);grid on;
stairs(coded);axis([0 100 -2 3]);
title('Encoded S/L');


qunt = reshape(coded, n,length(coded)/n);
index = bin2dec(num2str(qunt'));
q = delta*index+vmin+(delta/2);
subplot(2,1,2); grid on;
plot(q);
title('Demod S/L');