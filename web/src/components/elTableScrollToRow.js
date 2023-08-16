/*
感谢：程序员小山与Bug
https://github.com/sunzsh/vue-el-demo/blob/master/src/views/table-scroll-tr.vue
https://github.com/sunzsh/vue-el-demo/blob/master/src/utils/elTableScrollToRow.js
*/
export default function elTableScrollToRow(table, rowData) {
  const bodyWrapper = table.$el.querySelector('.el-scrollbar__wrap')
  const rowIndex = table.data.indexOf(rowData)
  const tr = bodyWrapper.querySelectorAll('tr')[rowIndex]
  if (!bodyWrapper || !tr) {
    return
  }
  console.log(bodyWrapper,tr,tr.offsetTop , tr.clientHeight , bodyWrapper.clientHeight)
  if (bodyWrapper.clientHeight + bodyWrapper.scrollTop < tr.offsetTop + tr.clientHeight || tr.offsetTop < bodyWrapper.scrollTop) {
    bodyWrapper.style.scrollBehavior = 'smooth'
    bodyWrapper.scrollTop = tr.offsetTop + tr.clientHeight - bodyWrapper.clientHeight
  }
}