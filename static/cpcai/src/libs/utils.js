export function now_str() {
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false // 24小时制
  };
  return new Date().toLocaleString('zh-CN', options).replace(/[/:]/g, "").replace(" ","")
}
