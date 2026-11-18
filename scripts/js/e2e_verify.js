const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  const routes = [
    { path: 'http://localhost:8088/index.html', title: 'MAYASTRA NAWALOKA', active: 'home' },
    { path: 'http://localhost:8088/about.html', title: 'About', active: 'about' },
    { path: 'http://localhost:8088/service.html', title: 'Services', active: 'service' },
    { path: 'http://localhost:8088/contact.html', title: 'Contact', active: 'contact' }
  ];

  for (const route of routes) {
    console.log(`Checking route: ${route.path}...`);
    await page.goto(route.path, { waitUntil: 'networkidle' });
    
    // 1. Check title
    const pageTitle = await page.title();
    console.log(`  Title: ${pageTitle}`);
    if (!pageTitle.includes(route.title)) throw new Error(`Title mismatch on ${route.path}`);

    // 2. Check WIB clock ticking
    const clockText = await page.textContent('#wibClock');
    console.log(`  Clock Text: ${clockText.trim()}`);
    if (!clockText.includes('WIB')) throw new Error(`WIB Clock missing on ${route.path}`);

    // 3. Check active nav link
    const activeLink = await page.locator(`.nav-link[data-page="${route.active}"]`).getAttribute('class');
    console.log(`  Active link class: ${activeLink}`);
    if (!activeLink.includes('active')) throw new Error(`Active class missing for ${route.active}`);

    // 4. Check footer original logo loaded
    const logoImg = page.locator('.giant-logo-image');
    const logoSrc = await logoImg.getAttribute('src');
    if (logoSrc !== 'assets/brand/logo.png') throw new Error(`Footer logo must be assets/brand/logo.png, got ${logoSrc}`);
    const nw = await logoImg.evaluate(el => el.naturalWidth);
    const nh = await logoImg.evaluate(el => el.naturalHeight);
    console.log(`  Footer Logo original photo: ${nw}x${nh}`);
    if (nw === 0) throw new Error(`Footer logo failed to load on ${route.path}`);
  }

  // About page specific: 3 team photos
  await page.goto('http://localhost:8088/about.html', { waitUntil: 'networkidle' });
  const teamImgs = await page.locator('.team-card-image img').all();
  console.log(`Team portraits count on about.html: ${teamImgs.length}`);
  if (teamImgs.length !== 3) throw new Error('Expected 3 team photos on about.html');
  for (let i = 0; i < 3; i++) {
    const tw = await teamImgs[i].evaluate(el => el.naturalWidth);
    console.log(`  Team member ${i+1}: ${tw}px naturalWidth`);
    if (tw === 0) throw new Error(`Team photo ${i+1} failed to load!`);
  }

  // Contact page specific: copy email
  await page.goto('http://localhost:8088/contact.html', { waitUntil: 'networkidle' });
  await page.click('#copyEmailBtn');
  const toast = page.locator('#toastNotice');
  await toast.waitFor({ state: 'visible' });
  const toastText = await toast.textContent();
  console.log(`Contact toast feedback: ${toastText.trim()}`);

  await browser.close();
  console.log('ALL 4 PAGES VERIFIED WITH ZERO ERRORS!');
})().catch(err => {
  console.error('E2E Test Failed:', err);
  process.exit(1);
});
