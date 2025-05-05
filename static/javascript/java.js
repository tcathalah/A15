document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('toggleTheme');
  

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
    }
  

    toggleBtn?.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const newTheme = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
    });
  

    document.addEventListener('keydown', (e) => {
      if (e.key.toLowerCase() === 's') {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });
  });
  