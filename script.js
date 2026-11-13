// MAYASTRA NAWALOKA - Interactive Functionality & Knowledge Engine
document.addEventListener('DOMContentLoaded', () => {
  // Modal Elements for Projects Preview (Homepage)
  const previewModal = document.getElementById('previewModal');
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
  const openPreviewModal = (projectKey) => {
    if (!previewModal) return;
    const data = projectData[projectKey];
    if (!data) return;

    if (modalImg) modalImg.src = data.src;
    if (modalImg) modalImg.alt = data.title;
    if (modalTitle) modalTitle.textContent = data.title;
    if (modalBadge) modalBadge.textContent = data.badge;
    if (modalMeta) modalMeta.textContent = data.meta;

    previewModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  // Close Preview Modal
  const closePreviewModal = () => {
    if (!previewModal) return;
    previewModal.classList.remove('active');
    document.body.style.overflow = '';
  };

  // Preview button click listeners
  document.querySelectorAll('.btn-preview').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const projectKey = btn.getAttribute('data-project');
      openPreviewModal(projectKey);
    });
  });

  // Clicking anywhere on project card opens preview
  document.querySelectorAll('.project-card').forEach((card) => {
    card.addEventListener('click', () => {
      const projectKey = card.getAttribute('data-project');
      openPreviewModal(projectKey);
    });
  });

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closePreviewModal);
  }

  if (previewModal) {
    previewModal.addEventListener('click', (e) => {
      if (e.target === previewModal) {
        closePreviewModal();
      }
    });
  }

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
    emailLink.addEventListener('click', () => {
      navigator.clipboard.writeText('contact@mayastranawaloka.com');
      showToast('OPENING MAIL AND COPIED ADDRESS');
    });
  }

  // Live Waktu Indonesia Barat (WIB / UTC+7) Clock
  const clockEl = document.getElementById('wibClock');
  if (clockEl) {
    const updateWibClock = () => {
      const now = new Date();
      const formatter = new Intl.DateTimeFormat('en-GB', {
        timeZone: 'Asia/Jakarta',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
      });
      const timeStr = formatter.format(now);
      const digits = clockEl.querySelector('.time-digits');
      if (digits) {
        digits.textContent = timeStr;
      } else {
        clockEl.textContent = `${timeStr} WIB`;
      }
    };
    updateWibClock();
    setInterval(updateWibClock, 1000);
  }

  // Active Navbar Link Detection
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach((link) => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });

  // ========================================================
  // ARTICLES ENGINE: DATA REPOSITORY & INTERACTIVE VIEWER
  // ========================================================
  const articlesDatabase = {
    1: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'NOV 2026 / 6 MIN READ',
      tags: '#ARCHITECTURE / #STATECHARTS / #DETERMINISM',
      title: 'Deterministic State Machines in Modern Web Applications',
      content: `
        <h4>1. The Perils of Ad-Hoc Boolean State</h4>
        <p>In modern web engineering, applications frequently accumulate fragmented boolean flags such as isLoading, isError, hasLoaded, and isSubmitting. As features compound, these combinations permit illegal states, such as isLoading and isError both evaluating to true simultaneously. This represents the primary vector for broken interfaces and race conditions.</p>
        <div class="article-modal-callout">
          <strong>Core Axiom:</strong> An interface can only reside in exactly one state at any discrete moment in time. State transitions must be explicit, mathematical, and deterministic.
        </div>
        <h4>2. Implementing Finite Statecharts</h4>
        <p>By formalizing views through finite state machines (FSM), engineers define explicit transition rules. A state can only transition to 'loading' via a 'FETCH' action, and from 'loading' exclusively to either 'success' or 'failure'. Unintended actions dispatched out of order are simply rejected by the state machine without corrupting memory.</p>
        <h4>3. Architectural Takeaway</h4>
        <p>At Mayastra Nawaloka, we enforce deterministic state definitions across client and server workflows. This guarantees that complex mission-critical dashboards remain robust under unreliable network latency and concurrent user interactions.</p>
      `
    },
    2: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'NOV 2026 / 8 MIN READ',
      tags: '#LINUX-KERNEL / #NETWORKING / #MEMORY',
      title: 'High-Throughput Memory Architecture and Zero-Copy I/O',
      content: `
        <h4>1. The Cost of Kernel-User Space Memory Copies</h4>
        <p>Standard networked applications read data from socket buffers into kernel space, copy those bytes into user-space application memory, modify buffers, and copy them back down into kernel space for socket transmission. Under high concurrency, these duplicated memory copies saturate L3 CPU cache lines and degrade throughput.</p>
        <h4>2. Zero-Copy Mechanics: sendfile and Memory Mapping</h4>
        <p>By leveraging Linux kernel primitives like the sendfile system call, splice, and mmap, servers transfer data directly from page caches to network interface cards without traversing user space. This eliminates intermediate copies and dramatically slashes CPU utilization.</p>
        <div class="article-modal-callout">
          <strong>Measured Impact:</strong> Eliminating user-space copy hops reduces per-packet CPU processing overhead by over 40 percent in high-throughput data distribution servers.
        </div>
        <h4>3. Production Application</h4>
        <p>We deploy zero-copy streaming pipelines within high-traffic enterprise media and asset distribution systems, ensuring sustained performance even during peak concurrent client requests.</p>
      `
    },
    3: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'OCT 2026 / 9 MIN READ',
      tags: '#DISTRIBUTED-DB / #RAFT / #LEDGER',
      title: 'Multi-Region Database Sharding and High-Concurrency Ledgers',
      content: `
        <h4>1. Distributed Ledger Partition Tolerance</h4>
        <p>In double-entry financial accounting and inventory ledger systems, write consistency is paramount. When data spans across multi-region datacenters, network partitions (split-brain scenarios) threaten data integrity. Systems must adhere strictly to the CAP theorem by favoring Consistency and Partition tolerance (CP) over unconstrained availability.</p>
        <h4>2. Raft Consensus and Monotonic Clocks</h4>
        <p>Distributed ledgers avoid clock skew anomalies by relying on monotonic logical clocks (Lamport timestamps or Hybrid Logical Clocks) paired with Raft leader consensus. Transactions are logged sequentially and cannot be reordered post-commit.</p>
        <div class="article-modal-callout">
          <strong>Key Rule:</strong> Never rely on raw server wall-clock timestamps for transaction ordering across distributed database clusters. Always bind ordering to deterministic logical sequences.
        </div>
        <h4>3. Enterprise Resilience</h4>
        <p>Our bespoke enterprise ledgers incorporate distributed Raft state clusters with deterministic sharding keys, ensuring financial records remain immutable and auditable across all operating branches.</p>
      `
    },
    4: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'OCT 2026 / 7 MIN READ',
      tags: '#ENGINEERING / #MONOLITH / #SYSTEMS',
      title: 'The Minimalist Monolith vs Premature Microservices',
      content: `
        <h4>1. The Organizational Tax of Microservices</h4>
        <p>Many mid-market organizations prematurely decompose their architecture into dozens of microservices. Instead of solving scaling bottlenecks, they introduce distributed network latency, difficult cross-service debugging, complex schema versioning, and expensive infrastructure overhead.</p>
        <h4>2. The Power of Modular Monoliths</h4>
        <p>A disciplined modular monolith delivers the clean boundary separation of microservices without the network latency tax. Modules interact via strictly typed internal interfaces. Memory calls execute in nanoseconds rather than HTTP or gRPC serialization hops taking milliseconds.</p>
        <div class="article-modal-callout">
          <strong>Empirical Finding:</strong> Teams maintaining modular monoliths consistently release features faster and maintain lower operational cloud expenditures than those managing fragmented microservices.
        </div>
        <h4>3. Strategic Scaling</h4>
        <p>Mayastra designs software architectures as highly cohesive modular monoliths. When a specific module genuinely requires independent hardware scaling, its strict interface enables extraction without requiring a total architectural rewrite.</p>
      `
    },
    5: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'OCT 2026 / 5 MIN READ',
      tags: '#WEBSOCKETS / #SSE / #REALTIME',
      title: 'Real-Time Distributed Events: WebSockets and Server-Sent Events',
      content: `
        <h4>1. Evaluating Real-Time Delivery Protocols</h4>
        <p>Developers often default to WebSockets for all real-time requirements. While WebSockets excel at bidirectional full-duplex communication (such as collaborative documents or gaming), they require custom heartbeat ping-pong logic and complex load-balancer connection state tracking.</p>
        <h4>2. The Elegant Simplicity of Server-Sent Events (SSE)</h4>
        <p>For scenarios where data flows primarily from server to client (stock tickers, notification streams, background task progress, live dashboards), Server-Sent Events over HTTP/2 provide automatic reconnection, built-in message IDs, and zero firewall traversal friction.</p>
        <div class="article-modal-callout">
          <strong>Protocol Rule:</strong> Prefer Server-Sent Events for unidirectional event streams. Reserve WebSockets specifically for high-frequency duplex client-server interactions.
        </div>
        <h4>3. Practical Implementation</h4>
        <p>We select the precise networking protocol tailored to the operational domain, avoiding unnecessary socket state management while delivering instantaneous telemetry updates.</p>
      `
    },
    6: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'SEP 2026 / 8 MIN READ',
      tags: '#SECURITY / #MTLS / #ZERO-TRUST',
      title: 'Zero-Trust Security Posture for Modern Corporate Infrastructure',
      content: `
        <h4>1. Abandoning Perimeter Castle-and-Moat Security</h4>
        <p>Traditional corporate networks assumed anyone inside the VPN perimeter was inherently trusted. Modern attack surfaces prove this model obsolete: once an attacker breaches a perimeter device, lateral movement across internal servers is trivial.</p>
        <h4>2. Implementing Continuous Cryptographic Verification</h4>
        <p>A zero-trust posture assumes the internal network is hostile. Every micro-service communication requires mutual TLS (mTLS) with cryptographically validated client certificates. Ephemeral tokens ensure authorization expires within minutes rather than months.</p>
        <div class="article-modal-callout">
          <strong>Security Principle:</strong> Never trust, always verify. Authenticate and authorize every transaction at both network and application boundaries.
        </div>
        <h4>3. Corporate Protection</h4>
        <p>Mayastra enforces zero-trust architecture across all deployed software systems: automated certificate rotation, non-root container runtimes, and strict cryptographic identity verification.</p>
      `
    },
    7: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'SEP 2026 / 6 MIN READ',
      tags: '#FRONTEND / #RENDERING / #PERFORMANCE',
      title: 'Eliminating Browser Layout Thrashing for 60 FPS Experiences',
      content: `
        <h4>1. The Anatomy of Layout Invalidation</h4>
        <p>When JavaScript code alternates between reading DOM geometric properties (such as offsetHeight or getBoundingClientRect) and writing style mutations, the browser engine is forced to compute synchronous layout cycles. This causes frame drops and sluggish rendering.</p>
        <h4>2. Batching Reads and Writes with requestAnimationFrame</h4>
        <p>Smooth 60 frames-per-second performance is achieved by separating read operations from write mutations. We batch geometric reads during the layout phase and apply style updates within requestAnimationFrame callbacks, leveraging CSS transform and opacity properties that bypass layout computation entirely.</p>
        <div class="article-modal-callout">
          <strong>Performance Standard:</strong> Limit visual animations strictly to compositor-only properties (transform and opacity) to guarantee GPU-accelerated 60 FPS transitions.
        </div>
        <h4>3. Design Standards</h4>
        <p>Every digital product built by Mayastra adheres to strict rendering discipline, ensuring instantaneous UI feedback and buttery-smooth responsiveness across mobile and desktop hardware.</p>
      `
    },
    8: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'AUG 2026 / 7 MIN READ',
      tags: '#EDGE-CDN / #CACHING / #LATENCY',
      title: 'Cache Coherence and Invalidation Strategies in Edge Networks',
      content: `
        <h4>1. The Invalidation Dilemma in Distributed CDNs</h4>
        <p>Distributing application responses across global edge servers reduces Time To First Byte (TTFB). However, ensuring that data updates on origin servers invalidate edge caches promptly without causing cache stampedes is a classic computer science challenge.</p>
        <h4>2. Surrogate Key Tagging and Stale-While-Revalidate</h4>
        <p>By tagging cached responses with granular surrogate keys, origin servers can instantly purge specific product or article caches globally via API. Concurrently, stale-while-revalidate headers serve cached content instantly while refreshing assets asynchronously in the background.</p>
        <div class="article-modal-callout">
          <strong>Target Metric:</strong> Sub-50ms global TTFB with guaranteed instant cache invalidation within 250ms of origin data updates.
        </div>
        <h4>3. Operational Integration</h4>
        <p>We configure intelligent edge routing and precise cache invalidation protocols, ensuring commercial stores and enterprise portals deliver blazing speed without serving outdated data.</p>
      `
    },
    9: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'AUG 2026 / 8 MIN READ',
      tags: '#DOCKER / #CGROUPS / #SANDBOX',
      title: 'Container Isolation and Ephemeral Linux Sandboxing Strategies',
      content: `
        <h4>1. The False Sense of Default Container Security</h4>
        <p>Running containers as root without resource constraints invites host compromise and Denial of Service (DoS) attacks. A single memory leak or rogue process can starve the host operating system of RAM and kernel file descriptors.</p>
        <h4>2. Enforcing cgroups v2 and Strict Sandboxing</h4>
        <p>We lock down application containers using Linux cgroups v2 to enforce hard 50 percent resource limits on CPU and RAM. Dropping all capabilities except those strictly required, applying seccomp filters, and mounting root filesystems as read-only closes container escape vectors.</p>
        <div class="article-modal-callout">
          <strong>Engineering Guideline:</strong> Containers must execute as unprivileged non-root users with read-only root filesystems and explicit memory limits.
        </div>
        <h4>3. Robust Systems</h4>
        <p>All runtime environments engineered by Mayastra implement hardened containerization protocols, safeguarding server stability and preventing noisy-neighbor degradation.</p>
      `
    },
    10: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'JUL 2026 / 6 MIN READ',
      tags: '#TYPE-SYSTEM / #RELIABILITY / #COMPILERS',
      title: 'Static Type Sovereignty: Eradicating Runtime Anomalies',
      content: `
        <h4>1. The Hidden Cost of Dynamic Type Exceptions</h4>
        <p>Null pointer dereferences, undefined is not a function, and silent type coercion anomalies constitute the overwhelming majority of production crashes in dynamically typed software. These errors waste engineering hours on reactive firefighting.</p>
        <h4>2. Making Illegal States Unrepresentable</h4>
        <p>By defining domain models with strict algebraic data types and exhaustive pattern matching, the compiler verifies all possible code branches before deployment. Invalid states cannot compile, transforming runtime bugs into immediate compile-time feedback.</p>
        <div class="article-modal-callout">
          <strong>Architectural Theorem:</strong> Structure your type definitions so that invalid business states cannot be represented in source code.
        </div>
        <h4>3. Engineering Rigor</h4>
        <p>Our engineering discipline mandates strict static type checks and schema validation at every external system boundary, ensuring mission-critical stability in production.</p>
      `
    },

    // ==================== HOW WE WORK ARTICLES (10) ====================
    11: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'NOV 2026 / 6 MIN READ',
      tags: '#WEB-DEV / #CUSTOM-WEB / #SEO-ENGINEERING',
      title: 'Bespoke Web Development: Delivering Ultra-Fast Commercial Platforms',
      content: `
        <h4>1. High-Performance Web Engineering for Growth Companies</h4>
        <p>Off-the-shelf website builders and bloated generic templates burden businesses with heavy JavaScript bundles, slow load speeds, and poor search engine crawlability. Mayastra Nawaloka engineers bespoke commercial web applications from the ground up to achieve maximum performance and Google search visibility.</p>
        <h4>2. Our Production Methodology</h4>
        <ul>
          <li><strong>Semantic HTML5 Architecture:</strong> Clean, structured semantic markup that search engine crawlers index with complete fidelity.</li>
          <li><strong>Sub-Second Load Times:</strong> Optimized asset pipelines, modern CSS styling, and zero bloated third-party framework overhead.</li>
          <li><strong>Responsive Ergonomics:</strong> Pixel-perfect display across high-resolution desktop monitors and mobile devices.</li>
          <li><strong>Conversion Optimization:</strong> Streamlined user pathways engineered to guide visitors toward inquiries and transactions.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Commercial Outcome:</strong> Our custom web applications consistently score 95+ on Google Core Web Vitals, elevating search rankings and driving organic business growth.
        </div>
        <h4>3. Partner With Us</h4>
        <p>Whether you require a flagship corporate portal or a high-converting commercial landing experience, our engineering team delivers software tailored precisely to your brand objectives.</p>
      `
    },
    12: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'NOV 2026 / 8 MIN READ',
      tags: '#ERP-SYSTEMS / #B2B-SOFTWARE / #OPERATIONS',
      title: 'Enterprise Resource Planning: Custom ERP for Scalable Operations',
      content: `
        <h4>1. Moving Beyond Generic ERP Limitations</h4>
        <p>Generic SaaS ERP platforms force growing enterprises into rigid, one-size-fits-all workflows while charging escalating per-seat monthly subscription fees. When business logic evolves, generic ERPs become cumbersome bottlenecks.</p>
        <h4>2. Custom ERP Modules Engineered by Mayastra</h4>
        <ul>
          <li><strong>Multi-Warehouse Inventory:</strong> Real-time SKU tracking, automated stock alerts, and multi-location transfer ledgers.</li>
          <li><strong>Procurement Automation:</strong> Purchase order generation, supplier approval workflows, and receiving logs.</li>
          <li><strong>Consolidated Financial Ledger:</strong> Automated invoice reconciliation, double-entry bookkeeping, and tax reporting.</li>
          <li><strong>Executive Analytics:</strong> Real-time operational dashboards visualizing revenue, margins, and warehouse turnover.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Strategic Value:</strong> Own your enterprise operating system outright with zero perpetual per-seat licensing fees and 100 percent customization to your workflows.
        </div>
        <h4>3. Built for Longevity</h4>
        <p>We build ERP systems that scale seamlessly with your organizational growth, providing complete operational independence and high-concurrency database reliability.</p>
      `
    },
    13: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'OCT 2026 / 7 MIN READ',
      tags: '#ECOMMERCE / #PAYMENTS / #CHECKOUT',
      title: 'High-Performance E-Commerce Development: Sub-Second Checkouts',
      content: `
        <h4>1. The Direct Link Between Checkout Speed and Revenue</h4>
        <p>Every 100 milliseconds of checkout latency costs online merchants real sales. Clunky shopping cart flows and slow payment redirects drive checkout abandonment. Our e-commerce engineering focuses on friction-free, instantaneous purchasing pipelines.</p>
        <h4>2. E-Commerce Capabilities We Deliver</h4>
        <ul>
          <li><strong>Sub-Second Product Filtering:</strong> Instant catalog search and facet filtering without full-page reloads.</li>
          <li><strong>Indonesian Payment Gateways:</strong> Native integration with QRIS, Virtual Accounts (BCA, Mandiri, BNI, BRI), e-wallets, and credit cards.</li>
          <li><strong>Resilient Order Ledgers:</strong> Transactional order locking preventing inventory overselling during promotional flash sales.</li>
          <li><strong>Automated Shipping Logistics:</strong> Live rate calculation and tracking status synchronization with national couriers.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Technical Guarantee:</strong> Zero checkout friction, sub-second transaction commits, and automatic real-time stock deduction.
        </div>
        <h4>3. Launch Your Custom Store</h4>
        <p>Partner with Mayastra to build a modern, high-speed boutique e-commerce platform that delights customers and turns traffic into loyal buyers.</p>
      `
    },
    14: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'OCT 2026 / 6 MIN READ',
      tags: '#CMS-DEVELOPMENT / #PUBLISHING / #EDITORIAL',
      title: 'Custom CMS Engineering: High-Density Publishing for Media & Brands',
      content: `
        <h4>1. Eliminating Content Publishing Friction</h4>
        <p>Editorial teams need clean, responsive authoring tools that let them focus on writing without fighting cumbersome backend dashboards or worrying about accidental formatting breakage.</p>
        <h4>2. Custom CMS Systems Engineered by Mayastra</h4>
        <ul>
          <li><strong>Focused Authoring Workspace:</strong> Distraction-free markdown and rich-text editing with instantaneous preview rendering.</li>
          <li><strong>Automated Asset Optimization:</strong> Images and media are automatically converted to next-generation formats (AVIF, WebP) upon upload.</li>
          <li><strong>Granular Role-Based Permissions:</strong> Tailored access levels for writers, editors, legal compliance, and administrators.</li>
          <li><strong>Built-in SEO Auditing:</strong> Live readability scores, canonical metadata validation, and OpenGraph social previews.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Efficiency Boost:</strong> Accelerate content production cycles by 60 percent with an authoring interface tailored specifically to your editorial workflow.
        </div>
        <h4>3. Elevate Your Media Brand</h4>
        <p>Let Mayastra construct a bespoke content management system that scales effortlessly with your publishing output and audience growth.</p>
      `
    },
    15: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'OCT 2026 / 8 MIN READ',
      tags: '#SOFTWARE-DEV / #FULLSTACK / #ENTERPRISE',
      title: 'Full-Stack Software Development: Custom Enterprise Web & Cloud',
      content: `
        <h4>1. Tailored Software That Solves Real Business Problems</h4>
        <p>When off-the-shelf software cannot satisfy your enterprise requirements, manual spreadsheets and fragmented communication tools take over, introducing costly errors and operational drag. Mayastra Nawaloka engineers bespoke full-stack software that automates core business processes.</p>
        <h4>2. Our Full-Lifecycle Engineering Approach</h4>
        <ul>
          <li><strong>Architectural Discovery:</strong> Mapping your exact operational domain, data flows, and security requirements.</li>
          <li><strong>API Contract Design:</strong> Establishing robust data contracts between frontend clients and backend micro-services.</li>
          <li><strong>Precision Development:</strong> Agile sprint execution backed by unit, integration, and end-to-end automated testing.</li>
          <li><strong>Production Deployment:</strong> Containerized staging and production environments with zero-downtime rollouts.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Quality Commitment:</strong> Every line of code is peer-reviewed, strictly typed, and verified through automated test suites prior to deployment.
        </div>
        <h4>3. Start Your Project</h4>
        <p>Bring your enterprise software vision to reality with a dedicated engineering partner committed to technical excellence and long-term business value.</p>
      `
    },
    16: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'SEP 2026 / 7 MIN READ',
      tags: '#CLOUD-DEVOPS / #CONTAINERS / #DEPLOYMENT',
      title: 'Cloud Infrastructure, Containerization, and Continuous Deployment',
      content: `
        <h4>1. Reliable Infrastructure for Mission-Critical Services</h4>
        <p>Server crashes, complicated manual deployments, and undocumented configuration drifts stall business growth. We architect predictable, automated cloud infrastructure that ensures 99.99 percent uptime.</p>
        <h4>2. DevOps & Infrastructure Standards We Enforce</h4>
        <ul>
          <li><strong>Immutable Docker Builds:</strong> Every deployment runs within isolated, reproducible Alpine Linux containers.</li>
          <li><strong>Resource Safety Caps:</strong> Explicit memory and CPU boundaries preventing system lockups and host starvation.</li>
          <li><strong>Automated CI/CD Pipelines:</strong> Code commits trigger automated linting, test suites, and zero-downtime rolling deploys.</li>
          <li><strong>SSL and Security Automation:</strong> Automated cryptographic certificate rotation and reverse proxy hardening.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Operational Result:</strong> Safe, automated deployments with instantaneous rollbacks and continuous server telemetry.
        </div>
        <h4>3. Modernize Your Infrastructure</h4>
        <p>Entrust your server infrastructure to Mayastra and achieve frictionless, automated deployments that keep your digital services online 24/7.</p>
      `
    },
    17: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'SEP 2026 / 6 MIN READ',
      tags: '#API-ENGINEERING / #INTEGRATION / #AUTOMATION',
      title: 'System Integration & API Engineering: Connecting Enterprise Stacks',
      content: `
        <h4>1. Unifying Fragmented Enterprise Data Silos</h4>
        <p>Modern enterprises rely on multiple specialized software tools: payment processors, warehouse scanners, third-party logistics, accounting packages, and CRM systems. Without seamless integration, staff waste countless hours manually copying data between disparate screens.</p>
        <h4>2. Integration Solutions We Build</h4>
        <ul>
          <li><strong>High-Security REST & GraphQL APIs:</strong> Secure, versioned endpoints with rate limiting and comprehensive documentation.</li>
          <li><strong>Asynchronous Webhook Queues:</strong> Resilient background worker pipelines with automated exponential backoff retries.</li>
          <li><strong>Third-Party Gateway Bridges:</strong> Direct synchronization with banking networks, logistics carriers, and government tax portals.</li>
          <li><strong>Audit Trail Logging:</strong> Immutable transaction logging for complete compliance and troubleshooting transparency.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Operational Gain:</strong> Eliminate data entry duplication, automate cross-platform reconciliation, and prevent human data entry errors.
        </div>
        <h4>3. Connect Your Ecosystem</h4>
        <p>Connect your business tools into a unified, automated operational engine with Mayastra's robust API engineering services.</p>
      `
    },
    18: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'AUG 2026 / 8 MIN READ',
      tags: '#MODERNIZATION / #DATA-MIGRATION / #REFACTORING',
      title: 'Legacy System Modernization and High-Assurance Data Migration',
      content: `
        <h4>1. Upgrading Critical Systems Without Downtime</h4>
        <p>Outdated legacy software exposes companies to security vulnerabilities and high maintenance costs. Yet migrating mission-critical systems carries significant operational risk. Mayastra specializes in zero-downtime system modernization.</p>
        <h4>2. Our High-Assurance Modernization Process</h4>
        <ul>
          <li><strong>The Strangler Fig Pattern:</strong> Incrementally replacing legacy modules piece-by-piece rather than attempting risky big-bang rewrites.</li>
          <li><strong>Dual-Write Verification:</strong> Running legacy and modern databases concurrently to verify 100 percent data parity before cutover.</li>
          <li><strong>Automated Data Sanitization:</strong> Cleaning legacy schema inconsistencies during database migration.</li>
          <li><strong>Zero Operational Disruption:</strong> Seamless cutovers scheduled during off-peak hours with full rollback plans.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Risk Mitigation:</strong> Complete data integrity verification with zero operational downtime and zero data loss.
        </div>
        <h4>3. Future-Proof Your Systems</h4>
        <p>Modernize your aging enterprise software into a fast, secure, modern platform while safeguarding your historical business data.</p>
      `
    },
    19: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'AUG 2026 / 7 MIN READ',
      tags: '#CODE-AUDIT / #SECURITY / #OPTIMIZATION',
      title: 'Performance Auditing, Code Optimization, and Security Hardening',
      content: `
        <h4>1. Uncovering Hidden Bottlenecks and Vulnerabilities</h4>
        <p>As commercial codebases grow, hidden database query bottlenecks, memory leaks, and outdated dependencies accumulate silently. Our comprehensive technical audit identifies and resolves performance and security issues before they affect users.</p>
        <h4>2. Scope of Our Technical Audits</h4>
        <ul>
          <li><strong>SQL Query Execution Profiling:</strong> Identifying unindexed table scans, N+1 query loops, and connection pool bottlenecks.</li>
          <li><strong>Security Vulnerability Scanning:</strong> Auditing source code against OWASP Top 10 vulnerabilities and dependency CVEs.</li>
          <li><strong>Bundle and Network Optimization:</strong> Minimizing frontend payload weights and eliminating render-blocking requests.</li>
          <li><strong>Actionable Remediation Roadmap:</strong> Providing clear, prioritized technical refactoring plans with measurable targets.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Measured Deliverable:</strong> Detailed technical audit documentation paired with immediate surgical performance patches.
        </div>
        <h4>3. Optimize Your Application</h4>
        <p>Request a technical audit from Mayastra to harden your application security, accelerate query speeds, and ensure your system is ready for scale.</p>
      `
    },
    20: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'JUL 2026 / 6 MIN READ',
      tags: '#PARTNERSHIP / #MAINTENANCE / #ENTERPRISE-SLA',
      title: 'Long-Term Technical Partnerships, SLA Support, and Software Evolution',
      content: `
        <h4>1. Technology as an Ongoing Strategic Asset</h4>
        <p>Software development does not end at initial launch. Operating systems update, security landscapes shift, and business needs continuously evolve. Mayastra establishes long-term engineering partnerships that protect your technology investments.</p>
        <h4>2. Partnership Benefits We Provide</h4>
        <ul>
          <li><strong>Guaranteed Service Level Agreements (SLA):</strong> Committed rapid response times for critical incident resolution.</li>
          <li><strong>Preventative Maintenance:</strong> Proactive security patch updates, database index re-tuning, and log rotation.</li>
          <li><strong>Continuous Feature Development:</strong> Dedicated development hours each month for iterative feature enhancements.</li>
          <li><strong>Disaster Recovery Drills:</strong> Regular automated backup verification and recovery simulations.</li>
        </ul>
        <div class="article-modal-callout">
          <strong>Peace of Mind:</strong> A dedicated, senior engineering team maintaining and advancing your software infrastructure year-round.
        </div>
        <h4>3. Collaborate With Mayastra</h4>
        <p>Partner with PT MAYASTRA NAWALOKA NUSANTARA as your trusted technical ally and empower your organization with enterprise-grade engineering excellence.</p>
      `
    }
  };

  // Article Modal Elements
  const articleModal = document.getElementById('articleModal');
  const articleModalTitle = document.getElementById('articleModalTitle');
  const articleModalBadge = document.getElementById('articleModalBadge');
  const articleModalMeta = document.getElementById('articleModalMeta');
  const articleModalBody = document.getElementById('articleModalBody');
  const articleModalTagSummary = document.getElementById('articleModalTagSummary');
  const articleModalCloseBtn = document.getElementById('articleModalCloseBtn');

  // Open Article Reader Modal
  const openArticleModal = (articleId) => {
    if (!articleModal) return;
    const article = articlesDatabase[articleId];
    if (!article) return;

    if (articleModalTitle) articleModalTitle.textContent = article.title;
    if (articleModalBadge) {
      articleModalBadge.textContent = article.badge;
      articleModalBadge.className = `article-category-badge ${article.category === 'insight' ? 'badge-insight' : 'badge-service'}`;
    }
    if (articleModalMeta) articleModalMeta.textContent = article.meta;
    if (articleModalTagSummary) articleModalTagSummary.textContent = article.tags;
    if (articleModalBody) articleModalBody.innerHTML = article.content;

    articleModal.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  // Close Article Reader Modal
  const closeArticleModal = () => {
    if (!articleModal) return;
    articleModal.classList.remove('active');
    document.body.style.overflow = '';
  };

  if (articleModalCloseBtn) {
    articleModalCloseBtn.addEventListener('click', closeArticleModal);
  }

  if (articleModal) {
    articleModal.addEventListener('click', (e) => {
      if (e.target === articleModal) {
        closeArticleModal();
      }
    });
  }

  // Bind clicks on all article cards
  document.querySelectorAll('.article-card').forEach((card) => {
    card.addEventListener('click', () => {
      const id = card.getAttribute('data-id');
      if (id) openArticleModal(id);
    });
  });

  // Category Filtering on articles.html
  const filterBtns = document.querySelectorAll('.filter-btn');
  const articleCards = document.querySelectorAll('.article-card');
  const searchInput = document.getElementById('articleSearchInput');

  const applyArticleFilters = () => {
    const activeBtn = document.querySelector('.filter-btn.active');
    const selectedFilter = activeBtn ? activeBtn.getAttribute('data-filter') : 'all';
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

    articleCards.forEach((card) => {
      const category = card.getAttribute('data-category');
      const text = card.textContent.toLowerCase();

      const matchesCategory = (selectedFilter === 'all' || category === selectedFilter);
      const matchesSearch = (!query || text.includes(query));

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  };

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      applyArticleFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', applyArticleFilters);
  }

  // Universal ESC key to close any active modal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      if (previewModal && previewModal.classList.contains('active')) {
        closePreviewModal();
      }
      if (articleModal && articleModal.classList.contains('active')) {
        closeArticleModal();
      }
    }
  });
});
