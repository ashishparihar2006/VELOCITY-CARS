import re
import glob

nav_replacement = r"""
    <a href="index.html" class="logo">VELOCITY</a>
    <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="models.html">Models</a></li>
        <li><a href="innovation.html">Innovation</a></li>
        <li><a href="services.html">Services</a></li>
    </ul>
    <div class="nav-actions" style="display: flex; align-items: center; gap: 20px;">
        <a href="profile.html" style="font-weight: 500; font-size: 0.9rem; transition: color 0.3s;" onmouseover="this.style.color='#e50914'" onmouseout="this.style.color='inherit'">Profile / Login</a>
        <a href="cart.html" style="font-weight: 500; font-size: 0.9rem; transition: color 0.3s;" onmouseover="this.style.color='#e50914'" onmouseout="this.style.color='inherit'">Cart (1)</a>
        <a href="index.html#contact" class="btn-nav">Book Test Drive</a>
    </div>
"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace contents of the navbar while keeping the opening and closing nav tags
    updated = re.sub(r'(<nav class="navbar"[^>]*>).*?(</nav>)', r'\1' + nav_replacement + r'\2', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f"Updated navbar in {file}")
