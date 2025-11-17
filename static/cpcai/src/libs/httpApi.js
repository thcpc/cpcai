import axios from 'axios'
axios.interceptors.request.use(
  (config) => {
    document.getElementById('overlay').classList.remove('d-none')
    return config
  },
  (error) => {
    // 对请求错误做些什么
    document.getElementById('overlay').classList.add('d-none')
    return Promise.reject(error)
  },
)

axios.interceptors.response.use(
  (response) => {
    // 对响应数据做些什么
    document.getElementById('overlay').classList.add('d-none')
    return response
  },
  (error) => {
    // 对响应错误做些什么
    document.getElementById('overlay').classList.add('d-none')
    return Promise.reject(error)
  },
)
export function httpGet(url, params, callBack) {
  axios.get(url, {
    params: params
  }).then(response => {
    httpResponse(response, callBack)
  })
    .catch(error => {
      console.error(error)
    })
}

export function httpPost(url, data, callBack){
  axios.defaults.headers.post["Content-Type"] = 'application/json'
  axios.post(url, data).then(response =>{
    httpResponse(response, callBack)
  }).catch(error=>{
    console.error(error)
  })
}

export function httpFormData(url, data, callBack){
  axios.defaults.headers.post["Content-Type"] = 'multipart/form-data'
  axios.post(url, data).then(response =>{
    httpResponse(response, callBack)
  }).catch(error=>{
    console.error(error)
  })
}


export function httpResponse(response, callBack){
  if(response.data.code === 200){
    callBack(response.data.payload)
  }else{
    alert(response.data.payload.err)
  }
}
