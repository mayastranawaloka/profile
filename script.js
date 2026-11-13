// MAYASTRA NAWALOKA - Interactive Functionality
document.addEventListener('DOMContentLoaded', () => {
  // Modal Elements
  const modal = document.getElementById('previewModal');
  const modalImg = document.getElementById('modalImage');
  const modalTitle = document.getElementById('modalTitle');
  const modalBadge = document.getElementById('modalBadge');
  const modalMeta = document.getElementById('modalMeta');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const toastNotice = document.getElementById('toastNotice');
  const copyEmailBtn = document.getElementById('copyEmailBtn');
  const emailLink = document.getElementById('emailLink');

  // Project data for modal preview
  const projectData = {
    erp: {
      title: 'ENTERPRISE RESOURCE PLANNING',
      badge: 'B2B OPERATIONS',
      meta: 'Multi-warehouse logistics, financial consolidation, and automated procurement pipeline.',
      src: 'assets/project-erp.svg'
    },
    ecommerce: {
      title: 'COMMERCE ARCHITECTURE',
      badge: 'DIRECT TO CONSUMER',
      meta: 'Curated boutique storefront, real-time cart ledger, and automated payment gateway.',
      src: 'assets/project-ecommerce.svg'
    },
    cms: {
      title: 'EDITORIAL CONTENT SYSTEM',
      badge: 'PUBLISHING PLATFORM',
      meta: 'High-density markdown workspace, live SEO analytics, and revision audit trail.',
      src: 'assets/project-cms.svg'
    }
  };

  // Open Preview Modal
  const openModal = (projectKey) => {
    const data = projectData[projectKey];
    if (!data) return;

    modalImg.src = data.src;
    modalImg.alt = data.title;
    modalTitle.textContent = data.title;
    modalBadge.textContent = data.badge;
    modalMeta.textContent = data.meta;

    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  // Close Preview Modal
  const closeModal = () => {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  };

  // Preview button click listeners
  document.querySelectorAll('.btn-preview').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const projectKey = btn.getAttribute('data-project');
      openModal(projectKey);
    });
  });

  // Clicking anywhere on card opens preview
  document.querySelectorAll('.project-card').forEach((card) => {
    card.addEventListener('click', () => {
      const projectKey = card.getAttribute('data-project');
      openModal(projectKey);
    });
  });

  // Modal Close interactions
  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeModal);
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal();
      }
    });
  }

  // Escape key to close modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });

  // Toast Helper
  let toastTimer = null;
  const showToast = (message) => {
    if (!toastNotice) return;
    toastNotice.textContent = message;
    toastNotice.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toastNotice.classList.remove('show');
    }, 2800);
  };

  // Copy Email Functionality
  const copyEmail = () => {
    const email = 'contact@mayastranawaloka.com';
    navigator.clipboard.writeText(email).then(() => {
      showToast('EMAIL COPIED TO CLIPBOARD');
    }).catch(() => {
      // Fallback for older browsers
      const textarea = document.createElement('textarea');
      textarea.value = email;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      showToast('EMAIL COPIED TO CLIPBOARD');
    });
  };

  if (copyEmailBtn) {
    copyEmailBtn.addEventListener('click', (e) => {
      e.preventDefault();
      copyEmail();
    });
  }

  if (emailLink) {
    emailLink.addEventListener('click', (e) => {
      // Allow default mailto, but also copy
      navigator.clipboard.writeText('contact@mayastranawaloka.com');
      showToast('OPENING MAIL & COPIED ADDRESS');
    });
  }
});
