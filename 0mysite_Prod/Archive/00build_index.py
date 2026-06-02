import os
import urllib.parse

def generate_index():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Store the top and bottom halves of your HTML
    html_top = """<!DOCTYPE html>
<html lang="en">
<body>
    <h1>🚀 My Galaxy J8 Server</h1>
    <h2>this server is hosted on an Android smartphone!</h2>
"""
    html_bottom = """
    <script>
      // Insert your dark mode script here
    </script>
</body>
</html>
"""
    
    dynamic_content = ""
    
    # Iterate through all items in the directory
    for item in sorted(os.listdir(base_dir)):
        item_path = os.path.join(base_dir, item)
        
        # We only care about directories, ignore hidden ones
        if os.path.isdir(item_path) and not item.startswith('.'):
            dynamic_content += f'\n    <h3 class="section-title">📁 {item}</h3>\n'
            dynamic_content += '    <div class="grid-container">\n'
            
            # Find all HTML files in this directory
            html_files = [f for f in sorted(os.listdir(item_path)) if f.endswith('.html')]
            
            for file in html_files:
                display_name = os.path.splitext(file)[0]
                # Safely encode the URL path
                folder_url = urllib.parse.quote(item)
                file_url = urllib.parse.quote(file)
                
                dynamic_content += f'      <div class="card">\n'
                dynamic_content += f'        <a href="{folder_url}/{file_url}">📄 {display_name}</a>\n'
                dynamic_content += f'      </div>\n'
                
            dynamic_content += '    </div>\n'

    # Write it all out to index.html
    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_top + dynamic_content + html_bottom)
        
    print("✅ index.html has been successfully generated!")

if __name__ == "__main__":
    generate_index()
