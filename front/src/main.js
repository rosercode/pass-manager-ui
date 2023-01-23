import Vue from 'vue'
import App from './App'
import axios from 'axios'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI)

//全局配置
axios.defaults.baseURL = 'http://127.0.0.1:5000/api';
// axios.defaults.baseURL = '/api';
Vue.prototype.$axios = axios
Vue.config.productionTip = false

// 重构 console.log 函数
const log = console.log
console.log = function(){
  if (process.env.NODE_ENV != "production"){
    log(...arguments)
  }
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
