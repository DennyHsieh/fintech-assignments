import os

per_data_folder = 'PER'
if not os.path.exists(per_data_folder):
    os.mkdir(per_data_folder)

os.chdir("./zh-NER-TF/")

# TODO: put the result to zh-NER-TF model
# os.system("python main.py --mode=demo --demo_model=1521112368")

