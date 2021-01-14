clc; close all;

data = [0 1 0 1 1 1 0 0 1 1];
figure
stem(data,'linewidth',3);grid on;
title('Tx data');axis([0 11 0 1.5]);grid on;

data_NRZ = 2*data-1;
s_p_data = reshape(data_NRZ,2,length(data)/2);

br = 10^6;
f = br;
T = 1/br;
t = T/99:T/99:T;

y =[];
y_in = [];
y_qd = [];
for(i=1:length(data)/2)
    y1 = s_p_data(1,i)*cos(2*pi*f*t);
    y2 = s_p_data(2,i)*sin(2*pi*f*t);
    y_in = [y_in y1];
    y_qd = [y_qd y2];
    y = [y y1+y2];
end

Tx_sig = y;
tt = T/99:T/99:(T*length(data))/2;

figure
subplot(3,1,1)
plot(tt,y_in,'linewidth',3);grid on;
title('Inphase QPSK');xlabel('Time(s)');ylabel('Amplitude(V)')
subplot(3,1,2)
plot(tt,y_qd,'linewidth',3);grid on;
title('Quadrature QPSK');xlabel('Time(s)');ylabel('Amplitude(V)')
subplot(3,1,3)
plot(tt,y,'r','linewidth',3);grid on;
title('QPSK');xlabel('Time(s)');ylabel('Amplitude(V)')

Rx_data = [];
Rx_sig = y;
for(i=1:1:length(data)/2)
    Z_in = Rx_sig((i-1)*length(t)+1:i*length(t)).*cos(2*pi*f*t);
    Z_in_intg =(trapz(t,Z_in))*(2/T);
    
    if(Z_in_intg > 0)
        Rx_in_data = 1;
    else
        Rx_in_data = 0;
    end
    
    Z_qd = Rx_sig((i-1)*length(t)+1:i*length(t)).*sin(2*pi*f*t);
    Z_qd_intg = (trapz(t,Z_qd))*(2/T);
    
    if(Z_qd_intg > 0)
        Rx_qd_data = 1;
    else
        Rx_qd_data = 0;
    end
    
    Rx_data = [Rx_data Rx_in_data Rx_qd_data];
end

figure
stem(Rx_data, 'linewidth', 3)
title('Rx S/L');
axis([0 11 0 1.5]);grid on;