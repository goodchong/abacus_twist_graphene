import os
import re
# 指定输入文件所在的目录
input_dir = 'origin'

# 指定输出文件所在的目录
output_dir = 'abacus-stru'

# 如果输出目录不存在,则创建它
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历输入目录中的所有文件
for filename in sorted(os.listdir(input_dir)):
    if filename.startswith('POSCAR.'):
        input_file = os.path.join(input_dir, filename)
        
        # 提取文件名中的数字部分
        numbers = re.split('[.-]', filename[7:]) #filename[7:].split('-')
        print(numbers)
        output_filename = f"graphene_{int(numbers[0]):02d}_{int(numbers[1]):02d}"
        output_file = os.path.join(output_dir, output_filename)
        
        # 读取输入文件
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # 解析数据
        lattice_vectors = []
        atomic_positions = []
        
        for i in range(2, 5):
            lattice_vectors.append(lines[i].split())
        
        num_atoms = int(lines[6])
        print(f"{output_filename}  Number of atoms: {num_atoms}")
        for i in range(8, 8 + num_atoms):
            atomic_positions.append(lines[i].split())
        
        # 写入输出文件
        with open(output_file, 'w') as file:
            file.write('ATOMIC_SPECIES\n')
            file.write('C 6.000 ./C_ONCV_PBE-1.0.upf\n\n')
            
            file.write('NUMERICAL_ORBITAL\n')
            file.write('./C_gga_8au_100Ry_2s2p1d.orb\n\n')
            
            file.write('LATTICE_CONSTANT\n')
            file.write('1.889716\n\n')
            
            file.write('LATTICE_VECTORS\n')
            for vector in lattice_vectors:
                file.write('       ' + '       '.join(vector) + '\n')
            file.write('\n')
            
            file.write('ATOMIC_POSITIONS\n')
            file.write('Direct\n\n')
            
            file.write('C\n')
            file.write('0.0\n')
            file.write(str(num_atoms) + '\n')
            for position in atomic_positions:
                file.write('     ' + '     '.join(position[:3]) + ' 1 1 1\n')
