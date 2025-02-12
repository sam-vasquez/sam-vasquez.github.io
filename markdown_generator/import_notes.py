import sys
import os
import re

def convert_to_url(title):
    urltitle = title.replace(" ","-").replace("=","-eq-").replace("≥","geq").replace("(","").replace(")","").replace("'","")
    return urltitle

def cleanup_content(content):
#   lines = content.split("\n")
    return content
    
#   for i in range(len(lines)):
#       line = lines[i]
#
#       # Replace Theorems
#       if line.startswith("> [!thm]"): 
#           line = f"**Theorem** ({line[8:]})."
#           j = 1
#           while i + j < len(lines) and lines[i+j].startswith(">"):
#               lines[i+j] = f"*{lines[i+j][1:]}*"
#               j += 1
#
#       # Replace Links
#       content = re.sub(r'\[\[(.*?)\|(.*?)\]\]', lambda match: f"[{match.group(2)}]({cleanup_title(match.group(1))})", content)



def process_directory(input_dir, output_dir, excluded_tags):
    for file in os.listdir(input_dir):
        curr_file_path = os.path.join(input_dir, file)

        if os.path.isdir(curr_file_path):
            process_directory(curr_file_path, output_dir, excluded_tags)
            continue

        if not file.endswith(".md"):
            continue 

        with open(curr_file_path, "r") as f:
            content = f.read()
            title = convert_to_url(file[:-3])

            if content.startswith("---\n") and len(content.split("---\n")) >= 3: # Contains YAML
                yaml = content.split("---\n")[1]
                main = content.split("---\n")[2] 

                excluded = False
                for tag in excluded_tags:
                    if tag in yaml: excluded = True
                if excluded: continue
                
                cleaned = cleanup_content(main)
                output = f"---\n{yaml}collection: notes\ntitle: \"{file[:-3]}\"\npermalink: /note/{title}/\n---\n{cleaned}"
            else: # Does not contain YAML 
                cleaned = cleanup_content(content)
                output = f"---\ncollection: notes\ntitle: \"{file[:-3]}\"\npermalink: /note/{title}/\n---\n{cleaned}"
        
        with open(os.path.join(output_dir, f"{title}.md"), "w") as g:
            g.write(output)
            print("Write Successful.")


if __name__ == '__main__':

    input_dir = os.path.join(os.getcwd(), os.path.normpath(sys.argv[1]))
    output_dir = os.path.join(os.getcwd(), os.path.normpath(sys.argv[2]))

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    else:
        for f in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, f))

    excluded_tags = ["private","exclude","todo","Course","Seminar","paper","Book"]
    process_directory(input_dir, output_dir, excluded_tags)
    print("Import Successful.")
