<script setup lang="ts">
import { onMounted, ref } from 'vue'
import NewCoze from '@/components/modals/config/NewCoze.vue'
import NewWorkFlow from '@/components/modals/config/NewWorkFlow.vue'
import eventBus, { WorkFlowRefreshEvent, CozeRefreshEvent } from '@/libs/eventBus.js'
import { getCozes, getWorkflows } from '@/libs/gateway'

const cozes = ref([])
const workflows = ref([])

onMounted(() => {
  eventBus.$on(WorkFlowRefreshEvent, (params) => {
    getWorkflows({}, (resp) => {
      workflows.value = resp
    })
  })

  eventBus.$on(CozeRefreshEvent, (params) => {
    getCozes({}, (resp) => {
      cozes.value = resp
    })
  })

  getCozes({}, (resp) => {
    cozes.value = resp
  })
  getWorkflows({}, (resp) => {
    workflows.value = resp
  })
})
</script>

<template>
  <new-coze />
  <new-work-flow />
  <div class="page-body">
    <div class="container-xl">
      <div class="card">
        <div class="card-header">
          <ul class="nav nav-tabs card-header-tabs nav-fill" data-bs-toggle="tabs" role="tablist">
            <li class="nav-item" role="presentation">
              <a
                href="#tabs-coze"
                class="nav-link active"
                data-bs-toggle="tab"
                aria-selected="true"
                role="tab"
                >Coze</a
              >
            </li>
            <li class="nav-item" role="presentation">
              <a
                href="#tabs-work-flow"
                class="nav-link"
                data-bs-toggle="tab"
                aria-selected="false"
                role="tab"
                tabindex="-1"
                >WorkFlow</a
              >
            </li>
          </ul>
        </div>
        <div class="card-body">
          <div class="tab-content">
            <div class="tab-pane active show" id="tabs-coze" role="tabpanel">
              <button class="btn btn-primary" data-bs-target="#newCoze" data-bs-toggle="modal">
                新建
              </button>

              <div class="table-responsive">
                <table class="table table-vcenter card-table">
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>CozeKey</th>
                      <th class="w-1"></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(coze, index) in cozes" :key="index">
                      <td>{{ coze.name }}</td>
                      <td>{{ coze.key }}</td>
                      <td>编辑</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="tab-pane" id="tabs-work-flow" role="tabpanel">
              <button class="btn btn-primary" data-bs-target="#newWorkFlow" data-bs-toggle="modal">
                新建
              </button>
              <div class="table-responsive">
                <table class="table table-vcenter card-table">
                  <thead>
                    <tr>
                      <th>Name</th>
                      <th>WorkFlowID</th>
                      <th class="w-1"></th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(workflow, index) in workflows" :key="index">
                      <td>{{ workflow.name }}</td>
                      <td>{{ workflow.workflow_id }}</td>
                      <td>编辑</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
