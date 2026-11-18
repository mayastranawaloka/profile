// MAYASTRA NAWALOKA - Interactive Functionality & Knowledge Engine
const initMayastraApp = () => {
  const toastNotice = document.getElementById('toastNotice');
  const copyEmailBtn = document.getElementById('copyEmailBtn');
  const emailLink = document.getElementById('emailLink');

  // Direct Project Navigation (Strict Zero Popups)
  document.querySelectorAll('.project-card').forEach((card) => {
    card.addEventListener('click', (e) => {
      // If user clicked inside an <a> tag directly, let normal navigation occur
      if (e.target.closest('a')) return;
      const projectKey = card.getAttribute('data-project');
      if (projectKey) {
        const isPages = window.location.pathname.includes('/pages/');
        window.location.href = isPages ? `project-${projectKey}.html` : `pages/project-${projectKey}.html`;
      }
    });
  });

  document.querySelectorAll('.btn-preview').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const projectKey = btn.getAttribute('data-project');
      if (projectKey) {
        const isPages = window.location.pathname.includes('/pages/');
        window.location.href = isPages ? `project-${projectKey}.html` : `pages/project-${projectKey}.html`;
      }
    });
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

  // ========================================================
  // THEME ENGINE (Dark / Light Mode with SVG Palette Swapping)
  // ========================================================
  const themeToggleBtn = document.getElementById('themeToggleBtn');

  const swapSvgs = (theme) => {
    document.querySelectorAll('img').forEach((img) => {
      const src = img.getAttribute('src');
      if (!src) return;

      let newSrc = null;
      if (theme === 'light') {
        // Swap project SVGs (both showcases and detail screens)
        if (src.includes('projects/') && !src.includes('projects-light/')) {
          newSrc = src.replace('projects/', 'projects-light/');
        }
        // Swap indonesia map underlay (indonesia-map.svg -> indonesia-map-light.svg)
        else if (src.includes('indonesia-map.svg') && !src.includes('-light.svg')) {
          newSrc = src.replace('indonesia-map.svg', 'indonesia-map-light.svg');
        }
      } else {
        // Restore dark project SVGs
        if (src.includes('projects-light/')) {
          newSrc = src.replace('projects-light/', 'projects/');
        }
        // Restore dark indonesia map underlay
        else if (src.includes('indonesia-map-light.svg')) {
          newSrc = src.replace('indonesia-map-light.svg', 'indonesia-map.svg');
        }
      }

      if (newSrc && newSrc !== src) {
        img.loading = 'eager';
        img.setAttribute('src', newSrc);
      }
    });
  };

  const applyTheme = (theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('mayastra_theme', theme);
    if (themeToggleBtn) {
      const label = themeToggleBtn.querySelector('.theme-toggle-label');
      if (label) {
        label.textContent = theme === 'light' ? 'LIGHT' : 'DARK';
      }
    }
    swapSvgs(theme);
  };

  const savedTheme = localStorage.getItem('mayastra_theme') || 'dark';
  applyTheme(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const next = current === 'light' ? 'dark' : 'light';
      applyTheme(next);
      showToast(`THEME SWITCHED TO ${next.toUpperCase()}`);
    });
  }

  // Mobile Nav Overflow Menu (3-dots kebab)
  const navOverflowBtn = document.getElementById('navOverflowBtn');
  const navMenu = document.querySelector('.nav-menu');

  if (navOverflowBtn && navMenu) {
    navOverflowBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const isOpen = navMenu.classList.toggle('open');
      navOverflowBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close when clicking any nav link inside menu
    navMenu.querySelectorAll('.nav-link').forEach((link) => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        navOverflowBtn.setAttribute('aria-expanded', 'false');
      });
    });

    // Close when clicking outside
    document.addEventListener('click', (e) => {
      if (!navMenu.contains(e.target) && !navOverflowBtn.contains(e.target)) {
        if (navMenu.classList.contains('open')) {
          navMenu.classList.remove('open');
          navOverflowBtn.setAttribute('aria-expanded', 'false');
        }
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navMenu.classList.contains('open')) {
        navMenu.classList.remove('open');
        navOverflowBtn.setAttribute('aria-expanded', 'false');
        navOverflowBtn.focus();
      }
    });
  }

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

  // Live Waktu Indonesia Barat (WIB / UTC+7) Clock (Strictly No Dot)
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
        clockEl.textContent = `${timeStr} UTC+7`;
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
  // ARTICLES KNOWLEDGE ENGINE (20 ENTRIES: 10 INSIGHT + 10 HOW WE WORK)
  // ID-EN Casual Professional Tone & Complete Mathematical Rigor
  // ========================================================
  const articlesDatabase = {
    1: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'NOV 2026 / 6 MIN READ',
      tags: '#ARCHITECTURE / #STATECHARTS / #DETERMINISM',
      title: 'Deterministic State Machines in Modern Web Applications',
      content: `
        <h4>1. Bahaya Ad-Hoc Boolean State di Client-Side</h4>
        <p>Di aplikasi web modern, frontend sering kali menimbun banyak boolean flag terpisah seperti isLoading, isError, hasLoaded, dan isSubmitting. Seiring bertambahnya fitur, kombinasi variabel ini memicu illegal states, contohnya isLoading dan isError sama-sama bernilai true. Ini adalah akar masalah utama tampilan UI rusak dan timbulnya race conditions liar saat request lambat.</p>
        <div class="article-reader-callout">
          <strong>Aksioma Arsitektur:</strong> Tampilan antarmuka hanya boleh berada di tepat satu state pada satu satuan waktu. Transisi status wajib bersifat eksplisit, matematis, dan deterministik.
        </div>
        <h4>2. Implementasi Finite Statecharts</h4>
        <p>Dengan meresmikan status visual lewat finite state machines (FSM), tim engineer mendefinisikan aturan transisi yang tegas. Suatu state hanya bisa berpindah ke 'loading' via aksi 'FETCH', dan dari 'loading' hanya bisa menuju 'success' atau 'failure'. Aksi tak terduga yang terpanggil di luar urutan otomatis ditolak tanpa merusak alur data di memori browser.</p>
        <h4>3. Standar Engineering Mayastra</h4>
        <p>Di Mayastra Nawaloka, kita menegakkan status deterministik pada seluruh workflow client dan server. Ini menjamin aplikasi bisnis mission-critical tetap kokoh menghadapi lonjakan latency jaringan dan interaksi simultan pengguna tanpa glitch.</p>
      `
    },
    2: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'NOV 2026 / 8 MIN READ',
      tags: '#LINUX-KERNEL / #NETWORKING / #MEMORY',
      title: 'High-Throughput Memory Architecture and Zero-Copy I/O',
      content: `
        <h4>1. Biaya Mahal Kernel-to-User Space Memory Copy</h4>
        <p>Aplikasi jaringan standar membaca data dari socket buffer di kernel space, menyalin byte tersebut ke memori aplikasi (user-space), memodifikasi buffer, lalu menyalinnya kembali ke kernel space untuk transmisi socket. Di bawah concurrency tinggi, proses duplikasi memori ini menghabiskan jalur L3 CPU cache dan membuat throughput anjlok drastis.</p>
        <h4>2. Mekanisme Zero-Copy: sendfile dan Memory Mapping</h4>
        <p>Dengan memanfaatkan primitif kernel Linux seperti system call sendfile, splice, dan mmap, server mentransfer data langsung dari page cache ke kartu jaringan (NIC) tanpa harus melewati user-space. Ini mengeliminasi salinan intermediate dan memangkas penggunaan CPU secara drastis.</p>
        <div class="article-reader-callout">
          <strong>Empirical Benchmark:</strong> Menghilangkan salinan data di user-space memangkas beban CPU per-paket hingga lebih dari 40 persen pada server distribusi file berkecepatan tinggi.
        </div>
        <h4>3. Implementasi Produksi</h4>
        <p>Kita terapkan pipeline streaming zero-copy pada sistem distribusi aset korporat dan edge gateways, memastikan latency tetap di bawah threshold optimal bahkan saat traffic jutaan paket per detik.</p>
      `
    },
    3: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'OCT 2026 / 9 MIN READ',
      tags: '#DISTRIBUTED-DB / #RAFT / #LEDGER',
      title: 'Multi-Region Database Sharding and High-Concurrency Ledgers',
      content: `
        <h4>1. Toleransi Partisi pada Ledger Terdistribusi</h4>
        <p>Pada sistem double-entry accounting dan inventory ledger berskala besar, konsistensi penulisan adalah prioritas absolut. Ketika cluster database tersebar di beberapa region datacenter, partisi jaringan (kondisi split-brain) bisa mengancam integritas data. Sistem wajib tunduk pada prinsip CAP theorem dengan mengutamakan Consistency dan Partition tolerance (CP) di atas availability tanpa batas.</p>
        <h4>2. Raft Consensus dan Logical Clocks</h4>
        <p>Ledger terdistribusi menghindari anomali clock skew dengan mengandalkan monotonic logical clocks (Hybrid Logical Clocks) yang dipadukan dengan konsensus pemimpin Raft. Seluruh transaksi dicatat secara sekuensial dan tidak dapat diubah urutannya setelah di-commit.</p>
        <div class="article-reader-callout">
          <strong>Prinsip Inti:</strong> Jangan pernah bergantung pada raw server wall-clock untuk menentukan urutan transaksi pada database terdistribusi. Selalu ikat urutan penulisan ke sequence logis deterministik.
        </div>
        <h4>3. Ketangguhan Enterprise</h4>
        <p>Sistem ledger Mayastra mengadopsi cluster state Raft dengan sharding key deterministik, memastikan catatan finansial dan perpindahan stok inventori tetap immutable dan transparan untuk diaudit.</p>
      `
    },
    4: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'OCT 2026 / 7 MIN READ',
      tags: '#ENGINEERING / #MONOLITH / #SYSTEMS',
      title: 'The Minimalist Monolith vs Premature Microservices',
      content: `
        <h4>1. Pajak Kompleksitas Premature Microservices</h4>
        <p>Banyak organisasi mid-market terburu-buru memecah arsitektur mereka menjadi belasan microservices mandiri. Alih-alih menyelesaikan scaling bottleneck, mereka malah menghadapi latency jaringan antar-service, kesulitan debugging distributed tracing, kompleksitas skema kontrak API, dan tagihan server cloud yang melambung tinggi.</p>
        <h4>2. Kekuatan Disiplin Modular Monolith</h4>
        <p>Modular monolith yang terdisiplin memberikan batas pemisahan domain yang bersih tanpa terkena beban pajak latency jaringan. Komunikasi antar modul terjadi via fungsi internal bertipe ketat dalam hitungan nanodetik, bukan serialisasi HTTP atau gRPC yang memakan milidetik.</p>
        <div class="article-reader-callout">
          <strong>Temuan Empiris:</strong> Tim pengembang yang mengelola modular monolith terbukti merilis fitur baru lebih cepat dan menghemat pengeluaran infrastruktur hingga 50 persen dibanding tim yang terjebak microservices rumit.
        </div>
        <h4>3. Strategi Skalabilitas Mayastra</h4>
        <p>Kita merancang arsitektur aplikasi sebagai modular monolith yang sangat kohesif. Jika suatu modul secara objektif membutuhkan scaling hardware independen, batas interface yang rapi memungkinkan modul tersebut diekstrak tanpa harus merombak seluruh codebase.</p>
      `
    },
    5: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'OCT 2026 / 5 MIN READ',
      tags: '#WEBSOCKETS / #SSE / #REALTIME',
      title: 'Real-Time Distributed Events: WebSockets and Server-Sent Events',
      content: `
        <h4>1. Memilih Protokol Real-Time yang Tepat</h4>
        <p>Banyak developer langsung mengasumsikan WebSocket adalah satu-satunya solusi untuk semua kebutuhan real-time. Padahal, meski WebSocket sangat unggul untuk komunikasi dua arah (full-duplex) seperti collaborative canvas atau live chat, ia menuntut logic heartbeat ping-pong manual dan pengelolaan connection state yang berat di load balancer.</p>
        <h4>2. Kesederhanaan Elegan Server-Sent Events (SSE)</h4>
        <p>Untuk use-case di mana data mengalir satu arah dari server ke browser (seperti update status pesanan, notifikasi sistem, progress background jobs, atau dashboard metrik), Server-Sent Events di atas HTTP/2 menawarkan reconnect otomatis, ID pesan built-in, dan zero firewall blockage.</p>
        <div class="article-reader-callout">
          <strong>Pedoman Protokol:</strong> Utamakan Server-Sent Events untuk streaming data searah dari server ke client. Gunakan WebSocket hanya untuk interaksi duplex berfrekuensi tinggi.
        </div>
        <h4>3. Desain Responsif</h4>
        <p>Mayastra memilih protokol komunikasi secara presisi sesuai domain operasional fitur, mencegah overhead memori yang sia-sia sembari tetap menghadirkan data telemetry real-time secepat kilat.</p>
      `
    },
    6: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'SEP 2026 / 8 MIN READ',
      tags: '#SECURITY / #MTLS / #ZERO-TRUST',
      title: 'Zero-Trust Security Posture for Modern Corporate Infrastructure',
      content: `
        <h4>1. Meninggalkan Model Keamanan Perusahaan Tradisional</h4>
        <p>Model keamanan lawas mengasumsikan siapa pun yang berada di dalam jaringan internal VPN otomatis dianggap aman dan terpercaya. Di era serangan modern, perimeter ini rentan: sekali penyerang berhasil membobol satu perangkat di dalam kantor, mereka leluasa bergerak secara lateral ke server database.</p>
        <h4>2. Verifikasi Kriptografis Berkelanjutan</h4>
        <p>Postur Zero-Trust mengasumsikan jaringan internal sama bahayanya dengan internet publik. Setiap komunikasi antar-service wajib diverifikasi dengan mutual TLS (mTLS) menggunakan sertifikat klien yang sah. Token otorisasi dibuat ephemeral dengan masa berlaku hitungan menit, bukan token permanen berbulan-bulan.</p>
        <div class="article-reader-callout">
          <strong>Prinsip Keamanan:</strong> Never trust, always verify. Validasi identitas dan wewenang di setiap transaksi pada level jaringan maupun aplikasi.
        </div>
        <h4>3. Pengamanan Sistem Korporat</h4>
        <p>Kita menerapkan prinsip zero-trust pada seluruh infrastruktur klien: rotasi sertifikat otomatis, eksekusi container non-root, dan isolasi kredensial tingkat tinggi.</p>
      `
    },
    7: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'SEP 2026 / 6 MIN READ',
      tags: '#FRONTEND / #RENDERING / #PERFORMANCE',
      title: 'Eliminating Browser Layout Thrashing for 60 FPS Experiences',
      content: `
        <h4>1. Anatomi Layout Invalidation di Browser</h4>
        <p>Ketika kode JavaScript membaca ukuran geometri DOM (seperti offsetHeight atau getBoundingClientRect) lalu langsung menuliskan perubahan styling (seperti style.width), engine browser terpaksa menjalankan reflow sinkron secara berulang. Ini menyebabkan stutter, frame drop, dan antarmuka terasa berat.</p>
        <h4>2. Batching Operasi Read dan Write</h4>
        <p>Performa mulus 60 FPS tercapai dengan memisahkan operasi pembacaan dari penulisan. Seluruh pembacaan dikumpulkan di awal, sementara perubahan visual dieksekusi di dalam requestAnimationFrame callback menggunakan properti CSS transform dan opacity yang diakselerasi langsung oleh GPU.</p>
        <div class="article-reader-callout">
          <strong>Standar Rekayasa Visual:</strong> Batasi animasi visual pada properti compositor-only (transform dan opacity) untuk menjamin render mulus 60 FPS tanpa memicu reflow CPU.
        </div>
        <h4>3. Kerapian Antarmuka</h4>
        <p>Setiap antarmuka web yang dibangun Mayastra mengikuti disiplin render ketat, menghadirkan feedback instan dan navigasi super mulus di perangkat desktop maupun smartphone.</p>
      `
    },
    8: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'AUG 2026 / 7 MIN READ',
      tags: '#EDGE-CDN / #CACHING / #LATENCY',
      title: 'Cache Coherence and Invalidation Strategies in Edge Networks',
      content: `
        <h4>1. Dilema Invalidation pada CDN Terdistribusi</h4>
        <p>Menyimpan salinan respons web di ratusan server edge global memangkas Time To First Byte (TTFB). Namun, memastikan bahwa perubahan data di server origin langsung menghapus cache di seluruh edge tanpa memicu gelombang request mendadak (cache stampede) adalah tantangan klasik sistem komputer.</p>
        <h4>2. Surrogate Key Tagging dan Stale-While-Revalidate</h4>
        <p>Dengan melabeli respons menggunakan surrogate keys granular, server origin dapat memicu purge cache secara instan via API untuk produk atau artikel tertentu. Pada saat yang sama, header stale-while-revalidate menyajikan konten cache yang ada seketika sambil memperbarui data di background secara asinkron.</p>
        <div class="article-reader-callout">
          <strong>Target Metrik:</strong> TTFB global di bawah 50ms dengan garansi invalidasi cache origin dalam tempo kurang dari 250ms saat terjadi pembaruan data bisnis.
        </div>
        <h4>3. Integrasi Operasional</h4>
        <p>Kita mengonfigurasi arsitektur routing edge cerdas sehingga etalase online dan portal informasi klien menyajikan performa ultra cepat tanpa pernah menampilkan data usang.</p>
      `
    },
    9: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'AUG 2026 / 8 MIN READ',
      tags: '#DOCKER / #CGROUPS / #SANDBOX',
      title: 'Container Isolation and Ephemeral Linux Sandboxing Strategies',
      content: `
        <h4>1. Bahaya Default Docker Container yang Berjalan sebagai Root</h4>
        <p>Menjalankan container sebagai root tanpa pembatasan resource membuka celah eksploitasi kernel dan Denial of Service. Satu memory leak atau proses liar dapat menguras RAM host Ubuntu dan mematikan daemon penting lainnya di server.</p>
        <h4>2. Penegakan cgroups v2 dan Hard Sandboxing</h4>
        <p>Kita mengunci runtime container menggunakan Linux cgroups v2 dengan batas keras alokasi CPU dan memori maksimal 50 persen hardware host. Menghapus semua capabilities Linux yang tidak esensial, menerapkan seccomp profile, dan me-mount root filesystem secara read-only menutup rapat celah pelarian container.</p>
        <div class="article-reader-callout">
          <strong>Aturan Isolasi:</strong> Kontainer wajib berjalan di bawah user non-root unprivileged dengan filesystem utama read-only dan batas resource tegas.
        </div>
        <h4>3. Stabilitas Server Jangka Panjang</h4>
        <p>Semua environment produksi Mayastra dirancang dengan pengerasan container menyeluruh, menjamin kestabilan host OS dan mencegah interferensi antar proses.</p>
      `
    },
    10: {
      category: 'insight',
      badge: 'INSIGHT',
      meta: 'JUL 2026 / 6 MIN READ',
      tags: '#TYPE-SYSTEM / #RELIABILITY / #COMPILERS',
      title: 'Static Type Sovereignty: Eradicating Runtime Anomalies',
      content: `
        <h4>1. Kerugian Tersembunyi dari Dynamic Type Crash</h4>
        <p>Pesan error seperti 'undefined is not a function' dan kesalahan konversi tipe data implisit menyumbang mayoritas crash di lingkungan produksi. Bug ini membuang waktu engineering berharga untuk investigasi panik setelah aplikasi terlanjur mengalami downtime.</p>
        <h4>2. Menjadikan Status Ilegal Mustahil Dikompilasi</h4>
        <p>Dengan mendefinisikan model domain menggunakan algebraic data types dan exhaustive pattern matching, compiler memeriksa seluruh kemungkinan alur kode sebelum dideploy. Status yang tidak valid tidak akan pernah bisa lolos proses compile, mengubah potensi bug runtime menjadi feedback seketika saat coding.</p>
        <div class="article-reader-callout">
          <strong>Teorema Arsitektur:</strong> Bangun struktur tipe data sedemikian rupa sehingga kondisi bisnis yang ilegal mustahil dituliskan di dalam source code aplikasi.
        </div>
        <h4>3. Kualitas Kode Mayastra</h4>
        <p>Disiplin engineering kami mewajibkan validasi tipe data statis ketat di setiap batas input eksternal, menjamin keandalan sistem berskala enterprise tanpa anomali mengejutkan di produksi.</p>
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
        <h4>1. Rekayasa Web Kustom untuk Bisnis Modern</h4>
        <p>Template instan dan website builder sering membebani perusahaan dengan bundle JavaScript yang membengkak, loading lambat, dan struktur kode yang sulit di-crawl oleh Google. Di Mayastra Nawaloka, kita merancang platform web komersial secara custom dari nol untuk menghasilkan kecepatan maksimal dan visibilitas search engine yang unggul.</p>
        <h4>2. Metodologi Produksi Mayastra</h4>
        <ul>
          <li><strong>Arsitektur Semantik HTML5:</strong> Struktur kode yang rapi dan terstandar, memudahkan mesin pencari mengindeks informasi bisnis secara presisi.</li>
          <li><strong>Loading Secepat Kilat (Sub-Second):</strong> Optimalisasi pipeline aset, modern vanilla CSS, dan tanpa bloat library pihak ketiga yang sia-sia.</li>
          <li><strong>Ergonomi Responsif Sempurna:</strong> Tampilan tajam dan proporsional di seluruh ukuran layar, mulai monitor 4K hingga smartphone ringkas.</li>
          <li><strong>Optimasi Conversion Flow:</strong> Jalur interaksi pengguna yang intuitif, dirancang untuk meningkatkan kontak masuk dan transaksi bisnis.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Hasil Bisnis Konkret:</strong> Aplikasi web bespoke kami secara konsisten meraih skor 95+ pada Google Core Web Vitals, mendongkrak peringkat SEO dan memperkuat citra kredibilitas perusahaan.
        </div>
        <h4>3. Kolaborasi Bareng Mayastra</h4>
        <p>Baik untuk portal korporat resmi maupun platform transaksi produk, tim engineer Mayastra siap menghadirkan solusi web berstandar teknologi internasional.</p>
      `
    },
    12: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'NOV 2026 / 8 MIN READ',
      tags: '#ERP-SYSTEMS / #B2B-SOFTWARE / #OPERATIONS',
      title: 'Enterprise Resource Planning: Custom ERP for Scalable Operations',
      content: `
        <h4>1. Mengatasi Keterbatasan ERP Generik di Pasaran</h4>
        <p>Sistem ERP generik sering memaksa perusahaan beradaptasi dengan alur kerja yang kaku, sembari mengenakan biaya langganan per-user bulanan yang semakin membengkak seiring bertambahnya tim kerja. Ketika proses bisnis berkembang, software generik justru menjadi penghambat utama.</p>
        <h4>2. Modul ERP Kustom Rancangan Mayastra</h4>
        <ul>
          <li><strong>Manajemen Multi-Gudang:</strong> Pelacakan inventori per nomor rak, transfer stok antar-cabang, dan peringatan minimum kuota otomatis.</li>
          <li><strong>Otomasi Pengadaan (Procurement):</strong> Pembuatan Purchase Order, alur approval bertingkat, dan pencatatan penerimaan barang di gudang.</li>
          <li><strong>General Ledger Terintegrasi:</strong> Rekonsiliasi faktur otomatis, pembukuan double-entry akuntansi, dan laporan keuangan komprehensif.</li>
          <li><strong>Executive Real-Time Dashboard:</strong> Visualisasi metrik arus kas, margin laba kotor, dan rasio perputaran barang gudang harian.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Kepemilikan Mutlak:</strong> Perusahaan Anda memiliki aset software ini secara 100 persen tanpa biaya royalti per-user, disesuaikan persis dengan alur kerja nyata operasional.
        </div>
        <h4>3. Dirancang untuk Skalabilitas Jangka Panjang</h4>
        <p>Kita membangun sistem ERP yang siap tumbuh bersama ekspansi bisnis Anda, memberikan independensi operasional penuh dan ketahanan database berkecepatan tinggi.</p>
      `
    },
    13: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'OCT 2026 / 7 MIN READ',
      tags: '#ECOMMERCE / #PAYMENTS / #CHECKOUT',
      title: 'High-Performance E-Commerce Development: Sub-Second Checkouts',
      content: `
        <h4>1. Hubungan Langsung Kecepatan Checkout dan Konversi Penjualan</h4>
        <p>Setiap penundaan 100 milidetik saat checkout berpotensi menurunkan konversi belanja. Alur pengisian data yang berbelit dan proses loading redirect pembayaran yang lama menjadi penyebab utama konsumen membatalkan pesanan. Fokus rekayasa e-commerce kami adalah menghadirkan alur transaksi yang instan dan tanpa gesekan.</p>
        <h4>2. Kapabilitas E-Commerce yang Kami Bangun</h4>
        <ul>
          <li><strong>Pencarian Katalog Instan:</strong> Filter produk dan pencarian kata kunci real-time di bawah 50 milidetik tanpa reload halaman.</li>
          <li><strong>Gateway Pembayaran Lengkap:</strong> Integrasi QRIS dinamis otomatis, Virtual Account semua bank utama, e-wallet, dan kartu debit/kredit internasional.</li>
          <li><strong>Penahanan Stok Transaksional:</strong> Penguncian kuota barang saat checkout dibuat untuk mencegah overselling saat periode flash sale.</li>
          <li><strong>Kalkulasi Ekspedisi Otomatis:</strong> Integrasi tarif ongkos kirim real-time dan update nomor resi pengiriman otomatis.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Garansi Teknis:</strong> Alur checkout satu langkah (one-page), commit database secepat kilat, dan sinkronisasi stok akurat secara real-time.
        </div>
        <h4>3. Luncurkan Toko Online Modern Anda</h4>
        <p>Bangun platform toko online headless berperforma tinggi bersama Mayastra untuk memberikan pengalaman belanja terbaik bagi para pelanggan Anda.</p>
      `
    },
    14: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'OCT 2026 / 6 MIN READ',
      tags: '#CMS-DEVELOPMENT / #PUBLISHING / #EDITORIAL',
      title: 'Custom CMS Engineering: High-Density Publishing for Media & Brands',
      content: `
        <h4>1. Menghapus Hambatan Penulisan di Ruang Redaksi</h4>
        <p>Tim editorial membutuhkan ruang penulisan yang cepat dan bebas distraksi, sehingga mereka bisa fokus menyusun naskah berkualitas tanpa harus bertarung dengan dashboard admin yang berat atau khawatir format teks rusak saat dipublikasikan.</p>
        <h4>2. Keunggulan Sistem CMS Rancangan Mayastra</h4>
        <ul>
          <li><strong>Workspace Markdown Ergonomis:</strong> Editor naskah berkecepatan tinggi dengan pratinjau live split-screen dan penyimpanan draft lokal instan.</li>
          <li><strong>Kompresi Aset Gambar Otomatis:</strong> Foto yang diunggah langsung dikonversi ke format modern (WebP/AVIF) dengan resolusi responsif.</li>
          <li><strong>Hierarki Perizinan Granular:</strong> Hak akses terstruktur untuk jurnalis pemula, editor bahasa, redaktur pelaksana, dan direksi editorial.</li>
          <li><strong>Audit SEO Terintegrasi:</strong> Evaluasi skor keterbacaan artikel, verifikasi canonical tag, dan pratinjau kartu OpenGraph sosial media.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Peningkatan Efisiensi:</strong> Percepat siklus penerbitan naskah hingga 60 persen dengan antarmuka yang dirancang khusus untuk ritme kerja redaksi Anda.
        </div>
        <h4>3. Kembangkan Publikasi Media Anda</h4>
        <p>Percayakan pembangunan sistem manajemen konten modern kepada Mayastra agar tim editorial Anda dapat bekerja lebih cepat dan terkoordinasi.</p>
      `
    },
    15: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'OCT 2026 / 8 MIN READ',
      tags: '#SOFTWARE-DEV / #FULLSTACK / #ENTERPRISE',
      title: 'Full-Stack Software Development: Custom Enterprise Web & Cloud',
      content: `
        <h4>1. Software Kustom untuk Menyelesaikan Masalah Operasional Riil</h4>
        <p>Ketika software generik di pasaran tidak mampu menjawab kebutuhan unik operasional perusahaan, spreadsheet manual dan koordinasi chat yang berserakan mengambil alih, memicu kesalahan input dan inefisiensi kerja. Mayastra merancang aplikasi full-stack kustom yang mengotomatisasi proses bisnis inti secara terpusat.</p>
        <h4>2. Pendekatan Rekayasa Software Mayastra</h4>
        <ul>
          <li><strong>Analisis Arsitektur Mendalam:</strong> Pemetaan menyeluruh alur data, kebutuhan keamanan, dan integrasi sistem eksisting perusahaan.</li>
          <li><strong>Desain Kontrak API Bertipe Ketat:</strong> Spesifikasi antarmuka yang jelas antara backend service dan aplikasi frontend.</li>
          <li><strong>Metodologi TDD Presisi:</strong> Pengembangan modular yang diverifikasi lewat unit test, integration test, dan end-to-end automated testing.</li>
          <li><strong>Deployment Berstandar Cloud:</strong> Lingkungan staging dan produksi terisolasi dengan proses rolling update tanpa downtime.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Komitmen Kualitas:</strong> Setiap baris kode ditinjau bersama (peer-reviewed), strictly typed, dan tervalidasi otomatis sebelum masuk ke server produksi.
        </div>
        <h4>3. Mulai Pengembangan Software Anda</h4>
        <p>Wujudkan kebutuhan software perusahaan bersama mitra teknologi yang berkomitmen pada keunggulan teknis dan nilai bisnis jangka panjang.</p>
      `
    },
    16: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'SEP 2026 / 7 MIN READ',
      tags: '#CLOUD-DEVOPS / #CONTAINERS / #DEPLOYMENT',
      title: 'Cloud Infrastructure, Containerization, and Continuous Deployment',
      content: `
        <h4>1. Fondasi Infrastruktur Andal untuk Layanan Bisnis Krusial</h4>
        <p>Server crash mendadak, proses deploy manual yang rumit, dan konfigurasi server yang tidak tercatat dapat melumpuhkan aktivitas bisnis. Kami merancang arsitektur cloud otomatis yang menjamin ketersediaan layanan hingga 99.99 persen uptime.</p>
        <h4>2. Standar DevOps yang Kami Tegakkan</h4>
        <ul>
          <li><strong>Build Container Imutabel:</strong> Setiap rilis aplikasi berjalan di dalam container Linux terisolasi dan dapat direproduksi secara deterministik.</li>
          <li><strong>Batas Keamanan Resource:</strong> Alokasi memori dan CPU terkontrol ketat untuk mencegah kelangkaan resource sistem host.</li>
          <li><strong>Pipeline CI/CD Otomatis:</strong> Setiap commit kode otomatis menjalankan linting, test suite, dan deployment bertahap tanpa downtime.</li>
          <li><strong>Otomasi Keamanan &amp; SSL:</strong> Rotasi sertifikat HTTPS terotomatisasi serta konfigurasi reverse proxy yang terlindungi.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Keunggulan Operasional:</strong> Proses deployment aman dengan opsi rollback instan dan pemantauan performa server secara berkelanjutan.
        </div>
        <h4>3. Modernisasi Infrastruktur Anda</h4>
        <p>Tingkatkan keandalan server perusahaan bersama Mayastra untuk memastikan seluruh layanan digital Anda berjalan lancar 24 jam non-stop.</p>
      `
    },
    17: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'SEP 2026 / 6 MIN READ',
      tags: '#API-ENGINEERING / #INTEGRATION / #AUTOMATION',
      title: 'System Integration & API Engineering: Connecting Enterprise Stacks',
      content: `
        <h4>1. Menghubungkan Silo Data Perusahaan yang Terfragmentasi</h4>
        <p>Perusahaan modern sering memakai beragam aplikasi spesifik: software akuntansi, payment gateway, pemindai barcode gudang, ekspedisi logistik, dan CRM. Tanpa integrasi otomatis, karyawan membuang waktu menyalin data manual antar sistem yang rawan kesalahan ketik.</p>
        <h4>2. Solusi Integrasi yang Kami Bangun</h4>
        <ul>
          <li><strong>API REST &amp; GraphQL Berkeamanan Tinggi:</strong> Titik integrasi dengan rate limiting, dokumentasi jelas, dan skema validasi ketat.</li>
          <li><strong>Antrean Webhook Asinkron:</strong> Pipeline pemrosesan background worker dengan retry otomatis dan exponential backoff jika terjadi kendala jaringan.</li>
          <li><strong>Jembatan Gateway Pihak Ketiga:</strong> Sinkronisasi langsung ke jaringan perbankan, portal logistik pengiriman, dan sistem eksternal mitra.</li>
          <li><strong>Pencatatan Audit Trail:</strong> Riwayat transaksi data lengkap untuk kemudahan audit dan penelusuran jika terjadi perbedaan angka.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Manfaat Operasional:</strong> Menghilangkan duplikasi entri data manual, mempercepat rekonsiliasi antar aplikasi, dan mencegah kesalahan manusia.
        </div>
        <h4>3. Integrasikan Ekosistem Bisnis Anda</h4>
        <p>Satukan seluruh aplikasi operasional perusahaan menjadi alur kerja terotomatisasi bersama layanan rekayasa API dari Mayastra.</p>
      `
    },
    18: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'AUG 2026 / 8 MIN READ',
      tags: '#MODERNIZATION / #DATA-MIGRATION / #REFACTORING',
      title: 'Legacy System Modernization and High-Assurance Data Migration',
      content: `
        <h4>1. Memperbarui Sistem Kritis Tanpa Gangguan Operasional</h4>
        <p>Aplikasi legacy yang usang membebani perusahaan dengan celah keamanan dan biaya pemeliharaan yang tinggi. Namun, merombak sistem yang sedang aktif menuntut kehati-hatian luar biasa agar operasional bisnis tidak terhenti. Mayastra memiliki keahlian khusus dalam modernisasi sistem dengan zero-downtime.</p>
        <h4>2. Metodologi Modernisasi Teruji</h4>
        <ul>
          <li><strong>Pola Strangler Fig:</strong> Mengganti modul lama secara bertahap dan terukur, bukan melakukan perombakan total yang berisiko tinggi.</li>
          <li><strong>Verifikasi Dual-Write:</strong> Menjalankan database lama dan database baru secara paralel untuk memastikan paritas data 100 persen sebelum beralih.</li>
          <li><strong>Pembersihan Data Otomatis:</strong> Merapikan ketidakkonsistenan skema data historis selama proses migrasi berlangsung.</li>
          <li><strong>Jadwal Cutover Terencana:</strong> Proses perpindahan final dijadwalkan pada jam non-operasional dengan skenario mitigasi rollback lengkap.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Mitigasi Risiko:</strong> Menjamin integritas data bisnis historis tanpa downtime dan tanpa risiko kehilangan catatan transaksi.
        </div>
        <h4>3. Siapkan Sistem Masa Depan Anda</h4>
        <p>Transformasikan software lama perusahaan menjadi platform modern yang cepat, aman, dan siap menopang ekspansi bisnis masa depan.</p>
      `
    },
    19: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'AUG 2026 / 7 MIN READ',
      tags: '#CODE-AUDIT / #SECURITY / #OPTIMIZATION',
      title: 'Performance Auditing, Code Optimization, and Security Hardening',
      content: `
        <h4>1. Mengidentifikasi Titik Lambat dan Celah Keamanan yang Tersembunyi</h4>
        <p>Seiring berkembangnya aplikasi, bottleneck query database yang lambat, kebocoran alokasi memori, dan dependensi pustaka yang usang sering terabaikan. Audit teknis independen membantu menemukan akar masalah performa dan keamanan sebelum berdampak pada pengguna nyata.</p>
        <h4>2. Ruang Lingkup Audit Teknis Mayastra</h4>
        <ul>
          <li><strong>Profiling Eksekusi Query Database:</strong> Mendeteksi table scan tanpa index, query loop N+1, dan bottleneck connection pool.</li>
          <li><strong>Pemindaian Celah Keamanan:</strong> Mengaudit celah kerentanan OWASP Top 10, sanitasi input, dan audit CVE pada dependensi proyek.</li>
          <li><strong>Optimalisasi Jaringan dan Bundle:</strong> Memangkas ukuran muatan frontend dan mengeliminasi script penghambat render.</li>
          <li><strong>Panduan Tindak Lanjut Terstruktur:</strong> Laporan hasil evaluasi komprehensif disertai rekomendasi solusi kode konkret yang siap dieksekusi.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Hasil Terukur:</strong> Dokumentasi audit teknis mendalam disertai perbaikan kode terarah yang meningkatkan kecepatan respon aplikasi secara nyata.
        </div>
        <h4>3. Optimalkan Aplikasi Anda</h4>
        <p>Jadwalkan audit teknis bersama tim senior engineer Mayastra untuk memastikan keandalan, kecepatan, dan ketahanan sistem digital Anda.</p>
      `
    },
    20: {
      category: 'how-we-work',
      badge: 'HOW WE WORK',
      meta: 'JUL 2026 / 6 MIN READ',
      tags: '#PARTNERSHIP / #MAINTENANCE / #ENTERPRISE-SLA',
      title: 'Long-Term Technical Partnerships, SLA Support, and Software Evolution',
      content: `
        <h4>1. Teknologi sebagai Aset Strategis Berkelanjutan</h4>
        <p>Pengembangan software tidak berhenti di hari peluncuran pertama. Sistem operasi terus diperbarui, pola ancaman keamanan terus berkembang, dan kebutuhan pasar selalu bergerak. Mayastra hadir sebagai mitra rekayasa teknologi jangka panjang yang menjaga keandalan investasi software Anda.</p>
        <h4>2. Layanan Kemitraan Jangka Panjang</h4>
        <ul>
          <li><strong>Komitmen Tanggap Insiden (SLA):</strong> Respons cepat dan terjamin untuk penanganan gangguan teknis darurat.</li>
          <li><strong>Pemeliharaan Preventif:</strong> Pembaruan patch keamanan rutin, tuning ulang index database, dan manajemen log berkala.</li>
          <li><strong>Pengembangan Fitur Berkelanjutan:</strong> Alokasi jam kerja tim engineer setiap bulan untuk iterasi dan peningkatan fitur baru.</li>
          <li><strong>Simulasi Pemulihan Bencana:</strong> Pengujian backup database otomatis secara berkala untuk memastikan data dapat dipulihkan kapan pun dibutuhkan.</li>
        </ul>
        <div class="article-reader-callout">
          <strong>Ketenangan Operasional:</strong> Didampingi tim engineer profesional yang siap merawat dan mengembangkan infrastruktur software Anda sepanjang tahun.
        </div>
        <h4>3. Bermitra Bersama Mayastra</h4>
        <p>Jadikan PT MAYASTRA NAWALOKA NUSANTARA sebagai mitra teknologi tepercaya untuk mendukung pertumbuhan dan keunggulan digital perusahaan Anda.</p>
      `
    }
  };

  // Standalone Article Reader Loader (article.html)
  const articleReaderView = document.getElementById('articleReaderView');
  if (articleReaderView) {
    const urlParams = new URLSearchParams(window.location.search);
    const rawId = urlParams.get('id');
    const articleId = rawId && articlesDatabase[rawId] ? parseInt(rawId, 10) : 1;
    const article = articlesDatabase[articleId] || articlesDatabase[1];

    const categoryBadge = document.getElementById('articleCategoryBadge');
    const metaEl = document.getElementById('articleMeta');
    const titleEl = document.getElementById('articleTitle');
    const tagsEl = document.getElementById('articleTags');
    const bodyEl = document.getElementById('articleBody');

    if (categoryBadge) {
      categoryBadge.textContent = article.badge;
      categoryBadge.className = `project-badge-pill ${article.category === 'insight' ? 'badge-insight' : 'badge-service'}`;
    }
    if (metaEl) metaEl.textContent = article.meta;
    if (titleEl) titleEl.textContent = article.title;
    if (tagsEl) tagsEl.textContent = article.tags;
    if (bodyEl) bodyEl.innerHTML = article.content;

    document.title = `${article.title} - MAYASTRA NAWALOKA`;

    // Dynamic SEO Updates for Search Crawlers and Share Cards
    const canonicalLink = document.querySelector('link[rel="canonical"]');
    if (canonicalLink) {
      canonicalLink.href = `https://www.mayastranawaloka.com/article.html?id=${articleId}`;
    }
    const metaDesc = document.querySelector('meta[name="description"]');
    if (metaDesc) {
      metaDesc.content = `${article.title}. Publikasi riset teknologi dan arsitektur sistem digital oleh PT Mayastra Nawaloka Nusantara.`;
    }
    const ogTitle = document.querySelector('meta[property="og:title"]');
    if (ogTitle) ogTitle.content = `${article.title} - MAYASTRA NAWALOKA`;
    const ogUrl = document.querySelector('meta[property="og:url"]');
    if (ogUrl) ogUrl.content = `https://www.mayastranawaloka.com/article.html?id=${articleId}`;
    const twTitle = document.querySelector('meta[name="twitter:title"]');
    if (twTitle) twTitle.content = `${article.title} - MAYASTRA NAWALOKA`;

    const schemaScript = document.getElementById('articleSchema');
    if (schemaScript) {
      try {
        const schema = JSON.parse(schemaScript.textContent);
        if (schema && schema['@graph'] && schema['@graph'][0]) {
          schema['@graph'][0].headline = article.title;
          schema['@graph'][0]['@id'] = `https://www.mayastranawaloka.com/article.html?id=${articleId}#article`;
          schema['@graph'][0].datePublished = '2026-11-14T08:00:00+07:00';
          schema['@graph'][0].dateModified = '2026-11-14T08:30:00+07:00';
          schemaScript.textContent = JSON.stringify(schema);
        }
      } catch (err) {
        // Fallback gracefully without throwing
      }
    }
  }

  // Articles Page: Category Filtering & Direct Card Clicks (articles.html)
  const filterBtns = document.querySelectorAll('.filter-btn');
  const articleCards = document.querySelectorAll('.article-card');
  const searchInput = document.getElementById('articleSearchInput');

  // Direct card navigation to standalone reader page (Strict Zero Popups)
  articleCards.forEach((card) => {
    card.addEventListener('click', (e) => {
      if (e.target.closest('a')) return;
      const id = card.getAttribute('data-id');
      if (id) {
        window.location.href = `article.html?id=${id}`;
      }
    });
  });

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
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMayastraApp);
} else {
  initMayastraApp();
}
