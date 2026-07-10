rm -f energy.yaml
rm -f peierlsstress.out
mkdir -p dump

mpirun -np 128 lmp -in applystress.in >> peierlsstress.out
