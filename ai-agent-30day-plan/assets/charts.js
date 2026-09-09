/* ==================================================================
   30 天 AI Agent 学习计划 · 图表脚本（ECharts）
   图 1：240 小时学习时间分配（与第 02 节正文数据一致）
   ================================================================== */
(function () {
  'use strict';

  function renderTimeAlloc() {
    var el = document.getElementById('chart-time-alloc');
    if (!el || typeof echarts === 'undefined') return;

    var C = { w1: '#4F46E5', w2: '#0EA5E9', w3: '#14B8A6', w4: '#7C3AED' };
    var TOTAL = 240;

    /* name, hours, days, week, color, isProject */
    var rows = [
      { name: 'Python 速成',        hours: 24, days: 'D1–3',      week: '第一周', color: C.w1, project: false },
      { name: 'LLM API 与 Prompt',  hours: 24, days: 'D4–6',      week: '第一周', color: C.w1, project: false },
      { name: 'Embedding 与向量库', hours: 8,  days: 'D7',        week: '第一周', color: C.w1, project: false },
      { name: 'LangChain / LangGraph', hours: 24, days: 'D8–10',  week: '第二周', color: C.w2, project: false },
      { name: '项目一 · 全能助手 Agent', hours: 32, days: 'D11–14', week: '第二周', color: C.w2, project: true },
      { name: 'RAG 实战与项目二',   hours: 32, days: 'D15–18',    week: '第三周', color: C.w3, project: true },
      { name: 'MCP 与平台认知',     hours: 16, days: 'D19–20',    week: '第三周', color: C.w3, project: false },
      { name: '周复盘与题库启动',   hours: 8,  days: 'D21',       week: '第三周', color: C.w3, project: false },
      { name: '项目三 · 数据分析多 Agent', hours: 32, days: 'D22–25', week: '第四周', color: C.w4, project: true },
      { name: '面试冲刺与投递',     hours: 32, days: 'D26–28、D30', week: '第四周', color: C.w4, project: false },
      { name: '查漏补强与总复盘',   hours: 8,  days: 'D29',       week: '第四周', color: C.w4, project: false }
    ];

    var chart = echarts.init(el);
    var ink = '#1A2233', muted = '#5D6B85';

    chart.setOption({
      backgroundColor: 'transparent',
      grid: { left: 8, right: 74, top: 10, bottom: 10, containLabel: true },
      tooltip: {
        trigger: 'item',
        backgroundColor: 'rgba(26,34,51,0.94)',
        borderWidth: 0,
        padding: [10, 14],
        textStyle: { color: '#fff', fontSize: 13 },
        formatter: function (p) {
          var d = rows[p.dataIndex];
          var share = Math.round((d.hours / TOTAL) * 100);
          return '<div style="font-weight:700;margin-bottom:4px;">' + d.name +
            (d.project ? ' <span style="color:#FBBF24;">★ 项目实战</span>' : '') + '</div>' +
            '<div>' + d.week + ' · ' + d.days + '</div>' +
            '<div style="margin-top:2px;">' + d.hours + ' 小时 · 占比 ' + share + '%</div>';
        }
      },
      xAxis: {
        type: 'value',
        axisLabel: { color: muted, fontSize: 11, formatter: '{value}h' },
        splitLine: { lineStyle: { color: '#E3E7F2', type: 'dashed' } }
      },
      yAxis: {
        type: 'category',
        inverse: true,
        data: rows.map(function (r) { return r.name; }),
        axisTick: { show: false },
        axisLine: { lineStyle: { color: '#E3E7F2' } },
        axisLabel: {
          color: ink, fontSize: 13, fontWeight: 600, margin: 12,
          formatter: function (v, i) {
            return v + (rows[i].project ? '  ★' : '');
          }
        }
      },
      series: [{
        type: 'bar',
        barWidth: 20,
        data: rows.map(function (r) {
          return {
            value: r.hours,
            itemStyle: {
              color: r.project
                ? { type: 'linear', x: 0, y: 0, x2: 1, y2: 0,
                    colorStops: [
                      { offset: 0, color: r.color },
                      { offset: 1, color: r.color + 'CC' }
                    ] }
                : r.color + 'D9',
              borderRadius: [0, 6, 6, 0]
            }
          };
        }),
        label: {
          show: true,
          position: 'right',
          color: muted,
          fontSize: 12,
          fontWeight: 700,
          formatter: function (p) {
            return p.value + 'h';
          }
        }
      }]
    });

    window.addEventListener('resize', function () { chart.resize(); });
  }

  function boot() {
    renderTimeAlloc();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
