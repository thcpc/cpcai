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

export function pyNewDoc(reqData, callBack) {
  loading()
  pywebview.api.newDoc(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyGetDoc(reqData, callBack){
  loading()
  pywebview.api.getDoc(reqData).then((result) => {
    pyResponse(result, callBack)
  });
}

export function pyRemoveDoc(reqData, callBack){
  loading()
  pywebview.api.removeDoc(reqData).then((result) => {
    pyResponse(result, callBack)
  });
}

export function pyGetLanguageLabel(reqData, callBack){
  loading()
  pywebview.api.getLanguageLabel().then((result) => {
    pyResponse(result, callBack)
  })
}


export function pyNewLanguage(reqData, callBack){
  loading()
  pywebview.api.newLanguage(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}


export function pyRelationshipLanguage(reqData, callBack){
  loading()
  pywebview.api.relationshipLanguage(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyDownloadFinalText(reqData, callBack){
  loading()
  pywebview.api.downloadFinalText(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyGetLanguage(reqData, callBack){
  loading()
  pywebview.api.getLanguage(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyDownLanguageXlsx(reqData, callBack){
  loading()
  pywebview.api.downLanguageXlsx(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyStartTranslate(reqData, callBack){
  loading()
  pywebview.api.startTranslate(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyDownTrDocx(reqData, callBack){
  loading()
  pywebview.api.downTrDocx(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}

export function pyDownTrPDF(reqData, callBack){
  loading()
  pywebview.api.downTrPDF(reqData).then((result) => {
    pyResponse(result, callBack)
  })
}


export function mock(on, real, fake) {
  if (on) {
    fake()
  } else {
    real()
  }
}

export function pyResponse(response, callBack) {
  if (response.code === 200) {
    loadingClosed()
    callBack(response.payload)
  } else {
    loadingClosed()
    alert(response.payload.err)
  }
}
