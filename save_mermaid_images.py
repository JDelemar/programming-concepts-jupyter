import os
import sys
import base64
import json
import re
from io import BytesIO
from PIL import Image
import nbformat
import requests

def save_mermaid_images(nb_path):
    # load notebook
    with open(nb_path) as f:
        nb = nbformat.read(f, as_version=4)

    # iterate over notebook cells
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            # find Mermaid code block
            mermaid_match = re.search('```mermaid(.+?)```', cell.source, re.DOTALL)

            if mermaid_match:
                mermaid_code = mermaid_match.group(1).strip()

                # Encode the mermaid code as a base64 encoded string
                encoded_bytes = base64.b64encode(mermaid_code.encode('utf-8'))
                encoded_string = encoded_bytes.decode('utf-8')

                # print("Encoded mermaid code:")
                # print(encoded_string)

                # generate Mermaid diagram as PNG image
                mermaid_url = f'https://mermaid.ink/img/{encoded_string}'
                response = requests.get(mermaid_url)
                
                # print("Response content:")
                # print(response.content)

                img = Image.open(BytesIO(response.content))

                # save PNG image to disk
                image_name = f'{nb_path.rsplit(".", 1)[0]}_mermaid.png'
                img.save(image_name)

                # replace Mermaid code block with Markdown image tag
                image_data = base64.b64encode(response.content).decode('utf-8')
                img_tag = f'![Diagram](data:image/png;base64,{image_data})'
                cell.source = re.sub('```mermaid(.+?)```', img_tag, cell.source, flags=re.DOTALL)

    # save updated notebook
    with open(nb_path, mode='w', encoding='utf-8') as f:
        nbformat.write(nb, f)


if __name__ == '__main__':
    # get notebook path from command-line argument
    nb_path = sys.argv[1]

    # save Mermaid images and update notebook
    save_mermaid_images(nb_path)
