/* ==================================================================
   30 天 AI Agent 学习计划 · 交互脚本
   进度追踪（localStorage 持久化）· 目录滚动高亮 · Mermaid 渲染
   ================================================================== */
(function () {
  'use strict';

  var STORE_KEY = 'agent30day-progress-v1';

  /* ---------------- 进度状态存取 ---------------- */
  function loadState() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function saveState(state) {
    try {
      localStorage.setItem(STORE_KEY, JSON.stringify(state));
    } catch (e) { /* 隐私模式等场景下静默失败 */ }
  }

  /* ---------------- 进度刷新 ---------------- */
  var boxes = Array.prototype.slice.call(document.querySelectorAll('.task input[type="checkbox"]'));
  var bar = document.querySelector('[data-progress-bar]');
  var pctText = document.querySelector('[data-progress-text]');
  var countText = document.querySelector('[data-progress-count]');
  var weekScopes = Array.prototype.slice.call(document.querySelectorAll('[data-week-scope]'));

  function refresh() {
    var total = boxes.length;
    var done = boxes.filter(function (b) { return b.checked; }).length;
    var pct = total ? Math.round((done / total) * 100) : 0;

    if (bar) bar.style.width = pct + '%';
    if (pctText) pctText.textContent = pct + '%';
    if (countText) countText.textContent = done + ' / ' + total;

    weekScopes.forEach(function (scope) {
      var countEl = scope.querySelector('[data-week-count]');
      if (!countEl) return;
      var scopeBoxes = Array.prototype.slice.call(scope.querySelectorAll('.task input[type="checkbox"]'));
      var scopeDone = scopeBoxes.filter(function (b) { return b.checked; }).length;
      countEl.textContent = scopeDone + ' / ' + scopeBoxes.length;
      scope.classList.toggle('week-complete', scopeBoxes.length > 0 && scopeDone === scopeBoxes.length);
    });
  }

  /* ---------------- 初始化勾选状态 ---------------- */
  var state = loadState();
  boxes.forEach(function (b) {
    if (state[b.id]) b.checked = true;
    b.addEventListener('change', function () {
      var s = loadState();
      if (b.checked) s[b.id] = 1; else delete s[b.id];
      saveState(s);
      refresh();
    });
  });
  refresh();

  /* ---------------- 重置进度 ---------------- */
  var resetBtn = document.getElementById('reset-progress');
  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      var ok = window.confirm('确定要清空全部勾选记录吗？此操作不可恢复。');
      if (!ok) return;
      try { localStorage.removeItem(STORE_KEY); } catch (e) {}
      boxes.forEach(function (b) { b.checked = false; });
      refresh();
    });
  }

  /* ---------------- 目录滚动高亮（Scroll Spy） ---------------- */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('#toc a'));
  var sections = tocLinks
    .map(function (a) { return document.querySelector(a.getAttribute('href')); })
    .filter(Boolean);

  function highlightTOC() {
    var pos = window.scrollY + 120;
    var current = sections[0];
    sections.forEach(function (sec) { if (sec.offsetTop <= pos) current = sec; });
    tocLinks.forEach(function (a) {
      a.classList.toggle('active', current && a.getAttribute('href') === '#' + current.id);
    });
  }
  window.addEventListener('scroll', highlightTOC, { passive: true });
  highlightTOC();

  /* ---------------- Mermaid 架构图渲染 ---------------- */
  function initMermaid() {
    if (typeof mermaid === 'undefined') return;
    mermaid.initialize({
      startOnLoad: false,
      theme: 'base',
      securityLevel: 'loose',
      fontFamily: "'Outfit', 'PingFang SC', 'Microsoft YaHei', sans-serif",
      themeVariables: {
        background: '#FFFFFF',
        primaryColor: '#EEF0FE',
        primaryTextColor: '#1A2233',
        primaryBorderColor: '#4F46E5',
        lineColor: '#5D6B85',
        secondaryColor: '#E4F5FD',
        tertiaryColor: '#E9FBF7',
        mainBkg: '#EEF0FE',
        nodeBorder: '#4F46E5',
        clusterBkg: 'rgba(246,247,251,0.9)',
        clusterBorder: '#E3E7F2',
        edgeLabelBackground: '#FFFFFF',
        fontSize: '14px'
      },
      flowchart: { curve: 'basis', padding: 14, useMaxWidth: true }
    });
    mermaid.run({ querySelector: 'pre.mermaid' }).catch(function (e) {
      console.warn('mermaid render failed:', e);
    });
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMermaid);
  } else {
    initMermaid();
  }
})();
