<script setup lang="ts">
import { ref } from 'vue'

const games = ref([
  {
    name: 'name',
    releaseDate:'',
    url: 'https://....',
    languages: "",
    supportPlatforms: "",
  },
  {
    name: 'name',
    releaseDate:'',
    url: 'https://....',
    language: "",
    supportPlatform: "",
  },
])
</script>

<template>
  <div class="page">
    <div class="page-wrapper">
      <div class="card">
        <div class="card-header">
          <div class="container">
            <div class="row">
              <div class="col-9">
                <div class="btn-group">
                  <button class="btn btn-primary">读取igdb</button>
                  <button class="btn btn-primary disabled">
                    素材下载
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="card-body">
          <table class="table table-selectable card-table table-vcenter text-nowrap datatable">
            <thead>
            <tr>
              <th class="w-1"><input class="form-check-input m-0 align-middle" type="checkbox" aria-label="Select all invoices"></th>
              <th>游戏名</th>
              <th>发售日期</th>
              <th>支持语言</th>
              <th>支持平台</th>
              <th>详情链接</th>
              <th></th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(game,index) in games" :key="index">
              <td><input class="form-check-input m-0 align-middle table-selectable-check" type="checkbox" aria-label="Select invoice"></td>
              <td>{{ game.name }}</td>
              <td>{{ game.releaseDate }}</td>
              <td>{{ game.languages }}</td>
              <td>{{ game.supportPlatforms}}</td>
              <td>{{ game.url}}</td>
              <td><button class="btn btn-primary disabled">详情</button></td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
