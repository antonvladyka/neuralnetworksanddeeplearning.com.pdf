z1 = -1*ones(size(z1));
z2 = 0*ones(size(z1));
z3 = 1*ones(size(z1));
z4 = (-5:0.01:5)';
Z = [z1 z2 z3 z4];
A = exp(Z);
s = repmat(sum(A,2),1,4);
a = A./s;
plot(z4,a);
legend({'a^L_1     z^L_1 = -1','a^L_2     z^L_2 = 0','a^L_3     z^L_3 = 1','a^L_4     z^L_4 = -5\ldots5'},'Location','Northwest')
xlabel('z^L_4')
ylabel('a^L_j')