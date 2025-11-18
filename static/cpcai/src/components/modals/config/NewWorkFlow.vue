<script setup lang="ts">
import { newWorkflow } from '@/libs/gateway'
import { ref } from 'vue'
import eventBus, {
  WorkFlowRefreshEvent,
} from '@/libs/eventBus.js'
const name =ref("")
const workflowId = ref("")


const newWorkFlow = ()=>{

  newWorkflow({name:name.value, workflowId:workflowId.value}, (resp)=>{
    eventBus.$emit(WorkFlowRefreshEvent, {})
    $('#newWorkFlow').modal('hide')
  })
}

</script>





<template>
  <div
    class="modal modal-blur fade"
    id="newWorkFlow"
    tabindex="-1"
    role="dialog"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">新的工作流配置</h5>
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
              placeholder="工作流名称"
              v-model="name"
            />
          </div>
          <div class="mb-3">
            <label class="form-label">WorkFlowID</label>
            <input
              type="text"
              class="form-control"
              name="example-text-input"
              placeholder="工作流ID"
              v-model="workflowId"
            />
          </div>
        </div>

        <div class="modal-footer">
          <a href="#" class="btn btn-link link-secondary btn-3" data-bs-dismiss="modal"> 取消 </a>
          <a href="#" class="btn btn-primary btn-5 ms-auto" @click="newWorkFlow()">
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
