rm energy.yaml
rm -f peierlsstress.out

for i in    200 250 300 350 400 425 450 500 550 ;
do

   mpirun -np 6 lmp -in applystress.in -var stress $i >> peierlsstress.out

done