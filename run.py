import os

def collect_mdx_content(root_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for dirpath, _, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith('.mdx'):
                    file_path = os.path.join(dirpath, filename)
                    outfile.write(f'--- File: {file_path} ---\n\n')
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                    outfile.write('\n\n')  # Separate contents of different files

if __name__ == "__main__":
    root_folder = "./books"  # Root folder where script is located
    output_file = os.path.join(root_folder, 'all_mdx_contents.txt')
    collect_mdx_content(root_folder, output_file)
    print(f"Collected .mdx contents saved to {output_file}")
