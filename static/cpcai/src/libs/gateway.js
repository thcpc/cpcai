import {httpFormData, httpGet, httpPost} from "@/libs/httpApi.js";
// import {
//   pyCompareExecute, pyDetailActive, pyDownLoad,
//   pyGetBuildInPackages,
//   pyDocs, pyGetCompareStudies, pyGetResult, pyInactivePackage,
//   pyNewCompare, pyNewPackage, pyQuickScan, pyRemoveCompares, pyValidBaselineName, pyNewDoc
// } from '@/libs/pyWebviewApi.js'

import {
 pyGetCoze, pyGetWorkFlow, pyNewCoze, pyNewWorkFlow, pyUpdateCoze
} from '@/libs/pyWebviewApi.js'

export const Event ="pywebviewready" // "DOMContentLoaded " //pywebviewready"
// export const Event = "DOMContentLoaded " //pywebviewready"
// export const proxyOn = true
export const proxyOn = true

export function OnMountedProxy(invoke){
  if(proxyOn){
    invoke()
  }else{
    window.addEventListener(Event, () => {
      invoke()
    })
  }
}

export function getCozes(reqData, callBack){
  (proxyOn === false) ?  pyGetCoze(reqData, callBack): httpGet("/api/coze/all",{}, callBack)
}

export function getWorkflows(reqData, callBack){
  (proxyOn === false) ?  pyGetWorkFlow(reqData, callBack): httpGet("/api/workflow/all",{}, callBack)
}

export function updateCoze(reqData, callBack){
  (proxyOn === false) ?  pyUpdateCoze(reqData, callBack): httpGet("/api/coze/set",{}, callBack)
}

export function newWorkflow(reqData, callBack){
  (proxyOn === false) ?  pyNewWorkFlow(reqData, callBack): httpPost("/api/workflow/new",reqData, callBack)
}
export function newCoze(reqData, callBack){
  (proxyOn === false) ?  pyNewCoze(reqData, callBack): httpPost("/api/coze/new",reqData, callBack)
}



// export function getCozes(reqData, callBack){
//   (proxyOn === false) ?  pyDocs(reqData, callBack): httpGet("/api/doc/all",{}, callBack)
// }





// export function getDocs(reqData, callBack){
//   (proxyOn === false) ?  pyDocs(reqData, callBack): httpGet("/api/doc/all",{}, callBack)
//
//
// }
//
// export function newDoc(reqData, callBack){
//   (proxyOn === false) ?  pyNewDoc(reqData, callBack): httpFormData("/api/doc/newDoc",reqData, callBack)
//
// }
//
//
// export function getLanguageLabel(reqData, callBack){
//   (proxyOn === false) ?  pyGetLanguageLabel(reqData, callBack): httpGet("/api/language/label",reqData, callBack)
// }
//
//
// export function newLanguage(reqData, callBack){
//   (proxyOn === false) ?  pyNewLanguage(reqData, callBack): httpFormData("/api/language/newLanguage",reqData, callBack)
// }
//
// export function relationshipLanguage(reqData,callBack){
//   (proxyOn === false) ? pyRelationshipLanguage(reqData, callBack): httpPost("/api/language/relationship", reqData, callBack)
// }
//
// export function downloadFinalText(reqData, callBack){
//   (proxyOn === false) ? pyDownloadFinalText(reqData, callBack): httpPost("/api/language/download_final", reqData, callBack)
//
// }
//
// export function getLanguage(reqData, callBack){
//   (proxyOn === false) ?  pyGetLanguage(reqData, callBack): httpPost("/api/language/get",reqData, callBack)
// }
//
// export function downloadLanguageXlsx(reqData, callBack){
//   (proxyOn === false) ? pyDownLanguageXlsx(reqData, callBack): httpPost("/api/language/download_xlsx", reqData, callBack)
// }
//
// export function startTranslate(reqData, callBack){
//   (proxyOn === false) ? pyStartTranslate(reqData, callBack): httpPost("/api/language/translate", reqData, callBack)
// }
//
// export function downTrDocx(reqData, callBack){
//   (proxyOn === false) ? pyDownTrDocx(reqData, callBack): httpPost("/api/language/download_docx_tr", reqData, callBack)
// }
//
// export function downTrPDF(reqData, callBack){
//   (proxyOn === false) ? pyDownTrPDF (reqData, callBack): httpPost("/api/language/download_pdf_tr", reqData, callBack)
// }
//
// export function getDoc(reqData, callBack){
//   (proxyOn === false) ? pyGetDoc(reqData, callBack): httpGet("/api/doc/get", reqData, callBack)
// }
//
// export function removeDoc(reqData, callBack){
//   (proxyOn === false) ? pyRemoveDoc(reqData, callBack): httpPost("/api/doc/remove", reqData, callBack)
// }
