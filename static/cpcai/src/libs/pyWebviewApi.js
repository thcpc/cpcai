const mockOn = false

function loading() {
  document.getElementById('overlay').classList.remove('d-none')
}

function loadingClosed() {
  document.getElementById('overlay').classList.add('d-none')
}

export function pyDocs(reqData, callBack) {
  // loading()
  pywebview.api.docs().then((result) => {
    if (result.code === 200) {
      // loadingClosed()
      callBack(result.payload)
    } else {
      // loadingClosed()
      alert(result.payload.err)
    }
  })
}

export function pyNewWorkFlow(reqData, callBack) {
  loading()
  pywebview.api.new_workflow(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyNewCoze(reqData, callBack){
  loading()
  pywebview.api.new_coze(reqData).then((result) => {
    pyResponse(result, callBack)
  });
}

export function pyUpdateCoze(reqData, callBack){
  loading()
  pywebview.api.update_coze(reqData).then((result) => {
    pyResponse(result, callBack)
  });
}

export function pyGetWorkFlow(reqData, callBack){
  loading()
  pywebview.api.get_work_flow().then((result) => {
    pyResponse(result, callBack)
  })
}


export function pyGetCoze(reqData, callBack){
  loading()
  pywebview.api.get_coze(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}


// export function pyRelationshipLanguage(reqData, callBack){
//   loading()
//   pywebview.api.relationshipLanguage(reqData).then((result) => {
//     pyResponse(result, callBack)
//   })
// }
//
// export function pyDownloadFinalText(reqData, callBack){
//   loading()
//   pywebview.api.downloadFinalText(reqData).then((result) => {
//     pyResponse(result, callBack)
//   })
// }
//
// export function pyGetLanguage(reqData, callBack){
//   loading()
//   pywebview.api.getLanguage(reqData).then((result) => {
//     pyResponse(result, callBack)
//   })
// }
//
// export function pyDownLanguageXlsx(reqData, callBack){
//   loading()
//   pywebview.api.downLanguageXlsx(reqData).then((result) => {
//     pyResponse(result, callBack)
//   })
// }
//
// export function pyStartTranslate(reqData, callBack){
//   loading()
//   pywebview.api.startTranslate(reqData).then((result) => {
//     pyResponse(result, callBack)
//   })
// }
//
// export function pyDownTrDocx(reqData, callBack){
//   loading()
//   pywebview.api.downTrDocx(reqData).then((result) => {
//     pyResponse(result, callBack)
//   })
// }
//
// export function pyDownTrPDF(reqData, callBack){
//   loading()
//   pywebview.api.downTrPDF(reqData).then((result) => {
//     pyResponse(result, callBack)
//   })
// }
//
//
// export function mock(on, real, fake) {
//   if (on) {
//     fake()
//   } else {
//     real()
//   }
// }

export function pyResponse(response, callBack) {
  if (response.code === 200) {
    loadingClosed()
    callBack(response.payload)
  } else {
    loadingClosed()
    alert(response.payload.err)
  }
}
