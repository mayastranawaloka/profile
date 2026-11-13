const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  console.log('Navigating to http://localhost:8088...');
  await page.goto('http://localhost:8088', { waitUntil: 'networkidle' });

  // 1. Verify Title & Hero
  const title = await page.title();
  console.log('Page Title:', title);
  if (!title.includes('MAYASTRA NAWALOKA')) throw new Error('Title mismatch');

  const heroText = await page.textContent('.hero-title');
  console.log('Hero Title Text:', heroText.trim());
  if (heroText.trim() !== 'MAYASTRA NAWALOKA') throw new Error('Hero text mismatch');

  // Verify No Navbar
  const navCount = await page.locator('nav').count();
  console.log('Nav element count:', navCount);
  if (navCount > 0) throw new Error('Navbar should not exist');

  // 2. Verify Projects Feed
  const cards = await page.locator('.project-card');
  const cardCount = await cards.count();
  console.log('Project card count:', cardCount);
  if (cardCount !== 3) throw new Error(`Expected 3 cards, got ${cardCount}`);

  // Test Hover on first card
  const firstCard = cards.nth(0);
  await firstCard.hover();
  const previewBtn = firstCard.locator('.btn-preview');
  await previewBtn.waitFor({ state: 'visible' });
  console.log('Hover state verified: Preview button became visible.');

  // Test Modal opening
  await previewBtn.click();
  const modal = page.locator('#previewModal');
  await modal.waitFor({ state: 'visible' });
  const modalTitle = await page.textContent('#modalTitle');
  console.log('Modal opened with title:', modalTitle.trim());

  // Test Modal closing via Escape
  await page.keyboard.press('Escape');
  await page.waitForTimeout(400);
  const isModalActive = await modal.evaluate(el => el.classList.contains('active'));
  console.log('Modal active after Escape:', isModalActive);
  if (isModalActive) throw new Error('Modal should close on Escape');

  // 3. Verify Contact Email
  const email = await page.textContent('.contact-email-link');
  console.log('Contact email:', email.trim());
  if (email.trim() !== 'contact@mayastranawaloka.com') throw new Error('Email mismatch');

  // Test Copy Email button
  await page.click('#copyEmailBtn');
  const toast = page.locator('#toastNotice');
  await toast.waitFor({ state: 'visible' });
  const toastText = await toast.textContent();
  console.log('Toast message:', toastText.trim());

  // 4. Verify Footer
  const footerCompany = await page.textContent('.footer-company-name');
  console.log('Footer company name:', footerCompany.trim());
  if (footerCompany.trim() !== 'BY. PT MAYASTRA NAWALOKA NUSANTARA') throw new Error('Footer info mismatch');

  // Verify Bottom Logo
  const giantLogo = page.locator('.giant-logo-image');
  const logoVisible = await giantLogo.isVisible();
  console.log('Bottom giant logo visible:', logoVisible);

  fs.mkdirSync('test-results', { recursive: true });
  await page.screenshot({ path: 'test-results/full-page.png', fullPage: true });
  console.log('Full-page screenshot saved to test-results/full-page.png');

  await browser.close();
  console.log('ALL E2E CHECKS PASSED PERFECTLY!');
})().catch(err => {
  console.error('E2E Test Failed:', err);
  process.exit(1);
});
