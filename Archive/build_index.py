import os
import urllib.parse

def generate_index():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
<<<<<<< HEAD
    # Store the top half of your HTML, including all styling and the theme toggle button
    html_top = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Android Server</title>
    <style>
      :root {
        --bg-color: #f0f0f0;
        --card-bg: white;
        --text-main: #333;
        --text-secondary: #666;
        --link-color: #333;
        --link-hover: #007bff;
        --shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      }

      body.dark {
        --bg-color: #0f172a;
        --card-bg: #1e293b;
        --text-main: #f1f5f9;
        --text-secondary: #94a3b8;
        --link-color: #f8fafc;
        --link-hover: #60a5fa;
        --shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
      }

      body {
        font-family: sans-serif;
        padding: 40px;
        background: var(--bg-color);
        color: var(--text-main);
        transition:
          background-color 0.3s ease,
          color 0.3s ease;
        margin: 0;
        position: relative;
      }

      h1 { margin-bottom: 10px; }
      h2 {
        font-weight: normal;
        color: var(--text-secondary);
        font-size: 1.1rem;
        margin-bottom: 30px;
      }
      .section-title {
        margin-top: 40px;
        border-bottom: 2px solid var(--text-secondary);
        padding-bottom: 10px;
      }

      .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 15px;
        margin-top: 20px;
      }

      .card {
        background: var(--card-bg);
        padding: 15px;
        border-radius: 12px;
        box-shadow: var(--shadow);
        transition:
          transform 0.2s,
          background-color 0.3s ease;
      }

      .card:hover { transform: translateY(-2px); }

      a {
        text-decoration: none;
        color: var(--link-color);
        font-weight: bold;
        font-size: 1rem;
        transition: color 0.2s;
        word-break: break-all;
      }

      a:hover { color: var(--link-hover); }

      .theme-toggle {
        position: absolute;
        top: 25px;
        right: 25px;
        background: var(--card-bg);
        border: none;
        cursor: pointer;
        padding: 10px;
        border-radius: 50%;
        box-shadow: var(--shadow);
        color: var(--text-main);
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
        z-index: 100;
      }

      @media (max-width: 600px) {
        body { padding: 20px; }
        .theme-toggle {
          top: 15px;
          right: 15px;
        }
      }
    </style>
  </head>
  <body>
    <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Dark Mode">
      <svg id="sun-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display: none">
        <circle cx="12" cy="12" r="5"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      </svg>
      <svg id="moon-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
      </svg>
    </button>

    <h1>🚀 My Galaxy J8 Server</h1>
    <h2>this server is hosted on an Android smartphone!</h2>
"""

    # Store the bottom half of your HTML, including the back button and Dark Mode JS
    html_bottom = """
    <div class="card" style="margin-top: 40px; text-align: center;">
      <a href="/">🏠 Back to Main Server Index</a>
    </div>

    <script>
      const toggleButton = document.getElementById("theme-toggle");
      const body = document.body;
      const sunIcon = document.getElementById("sun-icon");
      const moonIcon = document.getElementById("moon-icon");

      function updateIcons(isDark) {
        sunIcon.style.display = isDark ? "block" : "none";
        moonIcon.style.display = isDark ? "none" : "block";
      }

      const savedTheme = localStorage.getItem("theme");
      if (
        savedTheme === "dark" ||
        (!savedTheme &&
          window.matchMedia("(prefers-color-scheme: dark)").matches)
      ) {
        body.classList.add("dark");
        updateIcons(true);
      }

      toggleButton.addEventListener("click", () => {
        body.classList.toggle("dark");
        const isDark = body.classList.contains("dark");
        localStorage.setItem("theme", isDark ? "dark" : "light");
        updateIcons(isDark);
      });
    </script>
  </body>
=======
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
>>>>>>> a532ea77be0dbf5119e2402def7a5eee0da9cf54
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
<<<<<<< HEAD
                # This constructs the relative path exactly as needed (e.g., FolderName/FileName.html)
=======
>>>>>>> a532ea77be0dbf5119e2402def7a5eee0da9cf54
                dynamic_content += f'        <a href="{folder_url}/{file_url}">📄 {display_name}</a>\n'
                dynamic_content += f'      </div>\n'
                
            dynamic_content += '    </div>\n'

    # Write it all out to index.html
    with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_top + dynamic_content + html_bottom)
        
    print("✅ index.html has been successfully generated!")

if __name__ == "__main__":
<<<<<<< HEAD
    generate_index()
=======
    generate_index()
>>>>>>> a532ea77be0dbf5119e2402def7a5eee0da9cf54
