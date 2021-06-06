clear
clc

readData

U = u(:,:,:,1);
V = v(:,:,:,1);
W = w(:,:,:,1);

% load('U.mat')
% load('V.mat')
% load('W.mat')

eps = 1e-50;

amplsU = abs(fftn(U)/numel(U));
amplsV = abs(fftn(V)/numel(V));
amplsW = abs(fftn(W)/numel(W));

EK_U = amplsU.^2;
EK_V = amplsV.^2;
EK_W = amplsW.^2;

EK_U = fftshift(EK_U);
EK_V = fftshift(EK_V);
EK_W = fftshift(EK_W);

size_x = length(x);
size_y = length(y);
size_z = length(z);

box_x = size_x;
box_y = size_y;
box_z = size_z;

box_radius = int32(ceil((sqrt((box_x)^2+(box_y)^2+(box_z)^2))/2.)+1);

centerx = int32(box_x/2);
centery = int32(box_y/2);
centerz = int32(box_z/2);

EK_U_avsphr = zeros(box_radius, 1)+eps;
EK_V_avsphr = zeros(box_radius, 1)+eps;
EK_W_avsphr = zeros(box_radius, 1)+eps;

for i = 1:(box_x)
    for j = 1:(box_y)
        for k = 1:(box_z)
            temp = sqrt(double((i-centerx)^2+(j-centery)^2+(k-centerz)^2));
			wn =  int32(round(temp));
            wn = wn+1;
			EK_U_avsphr(wn) = EK_U_avsphr(wn) + EK_U(i, j, k);
			EK_V_avsphr(wn) = EK_V_avsphr(wn) + EK_V(i, j, k);
			EK_W_avsphr(wn) = EK_W_avsphr(wn) + EK_W(i, j, k);
        end
    end
end

EK_avsphr = 0.5*(EK_U_avsphr + EK_V_avsphr + EK_W_avsphr);

loglog((1:length(EK_avsphr)), EK_avsphr)

