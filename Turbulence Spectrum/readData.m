clear
clc

u = zeros(200,192,128,10);
v = zeros(200,192,128,10);
w = zeros(200,192,128,10);

n = 1;

for i = 100:20:280
    str1 = 'channel1_vel_t';
    str2 = num2str(i);
    str3 = '.dat';
    fileName = [str1,str2,str3];
    [f,x,y,z] = hybridReadRestart(fileName);
    u(:,:,:,n) = f(:,:,:,1);
    v(:,:,:,n) = f(:,:,:,2);
    w(:,:,:,n) = f(:,:,:,3);
    n = n+1;
end

clear f fileName i n str1 str2 str3