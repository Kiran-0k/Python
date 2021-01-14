clc;close all;

data = sign(randn(1,400));
T = 64;
dataup = upsample(data,T);

yrz = conv(dataup, [zeros(1,T/4), ones(1,T/2), zeros(1,T/4)]);
yrz = yrz(1:end-T+1);

ynrz = conv(dataup, ones(1,T));
ynrz = ynrz(1:end-T+1);

ysine = conv(dataup ,sin(pi*[0:T-1]/T));
ysine = ysine(1:end-T+1);

Td = 32;
yrcos = conv(dataup, rcosfir(0.5,Td,T,1,'normal'));
yrcos = yrcos(2*Td*T:end-2*Td*T+1);

eye1 = eyediagram(yrz, T, T, T/2);
title('RZ');
% xlim([-Td-2,Td+2]);
ylim([-1.5,1.5]);
grid on

eye2 = eyediagram(ynrz, T, T, T/2);
title('NRZ');
% xlim([-Td-2,Td+2]);
ylim([-1.5,1.5]);
grid on

eye3 = eyediagram(ysine, T, T, T/2);
title('Half-Sine');
% xlim([-Td-2,Td+2]);
ylim([-1.5,1.5]);
grid on

eye4 = eyediagram(yrcos, 2*T, T);
title('RC');
% xlim([-Td-2,Td+2]);
ylim([-1.5,1.5]);
grid on