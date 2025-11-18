<script setup lang="ts">
import eventBus, {

  CozeRefreshEvent
} from '@/libs/eventBus.js'
import { newCoze } from '@/libs/gateway'
import { ref } from 'vue'

const name =ref("")
const cozeKey = ref("")

const newCozeKey = ()=>{
  newCoze({name:name.value, cozeKey:cozeKey.value}, (resp)=>{
    eventBus.$emit(CozeRefreshEvent, {})
    $('#newCoze').modal('hide')
  })
}


</script>

<template>
  <div
    class="modal modal-blur"
    id="newCoze"
    tabindex="-1"
    role="dialog"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">新的 Coze Key </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="mb-3">
            <label class="form-label">Name</label>
            <input
              type="text"
              class="form-control"
              name="example-text-input"
              placeholder="扣子账号名"
              v-model="name"
            />
          </div>
          <div class="mb-3">
            <label class="form-label">CozeKey</label>
            <input
              type="text"
              class="form-control"
              name="example-text-input"
              placeholder="扣子 API Key"
              v-model="cozeKey"
            />
          </div>
        </div>

      <div class="modal-footer">
        <a href="#" class="btn btn-link link-secondary btn-3" data-bs-dismiss="modal"> 取消 </a>
        <a href="#" class="btn btn-primary btn-5 ms-auto" @click="newCozeKey()">
          <!-- Download SVG icon from http://tabler.io/icons/icon/plus -->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="icon icon-2"
          >
            <path d="M12 5l0 14"></path>
            <path d="M5 12l14 0"></path>
          </svg>
          创建
        </a>
      </div>
    </div>
  </div>
  </div>
</template>

<style scoped></style>
