<script setup>
import LoadingSpinner from '@/components/LoadingSpinner.vue'
</script>

<template>
  <loading-spinner/>
  <header class="navbar-expand-md">
    <div class="collapse navbar-collapse" id="navbar-menu">
      <div class="navbar">
        <div class="container-xl">
          <div class="row flex-column flex-md-row flex-fill align-items-center">
            <div class="col">
              <!-- BEGIN NAVBAR MENU -->
              <ul class="navbar-nav">
<!--                <li class="nav-item dropdown">-->
<!--                  <a-->
<!--                    class="nav-link dropdown-toggle"-->
<!--                    href="#navbar-form"-->
<!--                    data-bs-toggle="dropdown"-->
<!--                    data-bs-auto-close="outside"-->
<!--                    role="button"-->
<!--                    aria-expanded="false"-->
<!--                  >-->
<!--                    <span class="nav-link-icon d-md-none d-lg-inline-block"-->
<!--                      >&lt;!&ndash; Download SVG icon from http://tabler.io/icons/icon/home &ndash;&gt;-->
<!--                      <svg-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                        width="24"-->
<!--                        height="24"-->
<!--                        viewBox="0 0 24 24"-->
<!--                        fill="none"-->
<!--                        stroke="currentColor"-->
<!--                        stroke-width="2"-->
<!--                        stroke-linecap="round"-->
<!--                        stroke-linejoin="round"-->
<!--                        class="icon icon-1"-->
<!--                      >-->
<!--                        <path d="M5 12l-2 0l9 -9l9 9l-2 0"></path>-->
<!--                        <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7"></path>-->
<!--                        <path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6"></path></svg-->
<!--                    ></span>-->
<!--                    <span class="nav-link-title"> 游戏 </span>-->
<!--                    <div class="dropdown-menu">-->
<!--                      <a class="dropdown-item" href="./form-elements.html"> 游戏资讯 </a>-->
<!--                      <a class="dropdown-item" href="./form-layout.html">游戏小知识 </a>-->
<!--                    </div>-->
<!--                  </a>-->
<!--                </li>-->
                <li class="nav-item dropdown">
                  <a
                    class="nav-link dropdown-toggle"
                    data-bs-toggle="dropdown"
                    data-bs-auto-close="outside"
                    role="button"
                    aria-expanded="false"
                  >
                    <span class="nav-link-icon d-md-none d-lg-inline-block"><!-- Download SVG icon from http://tabler.io/icons/icon/home -->
                          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-1">
                            <path d="M5 12l-2 0l9 -9l9 9l-2 0"></path>
                            <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7"></path>
                            <path d="M9 21v-6a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v6"></path></svg></span>
                    <span class="nav-link-title"> 游戏 </span>
                  </a>
                  <div class="dropdown-menu">
                    <router-link to="/game" class="dropdown-item">游戏快报</router-link>
                    <router-link to="/gameKnowledge" class="dropdown-item">游戏小知识</router-link>
                  </div>
                </li>
                <li class="nav-item dropdown">
                  <a
                    class="nav-link dropdown-toggle"
                    data-bs-toggle="dropdown"
                    data-bs-auto-close="outside"
                    role="button"
                    aria-expanded="false"
                  >
                    <span class="nav-link-icon d-md-none d-lg-inline-block"
                      ><!-- Download SVG icon from http://tabler.io/icons/icon/checkbox -->
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
                        class="icon icon-1"
                      >
                        <path d="M9 11l3 3l8 -8"></path>
                        <path
                          d="M20 12v6a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12a2 2 0 0 1 2 -2h9"
                        ></path></svg
                    ></span>
                    <span class="nav-link-title"> 财经 </span>
                  </a>
                  <div class="dropdown-menu">
                    <router-link to="/game" class="dropdown-item">游戏快报</router-link>
                    <router-link to="/gameKnowledge" class="dropdown-item">游戏小知识</router-link>
                  </div>
                </li>
              </ul>
              <!-- END NAVBAR MENU -->
            </div>
            <div class="col col-md-auto">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <router-link to="/config" class="nav-link">
                    <span class="nav-link-icon d-md-none d-lg-inline-block">
                      <!-- Download SVG icon from http://tabler.io/icons/icon/settings -->
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
                        class="icon icon-1"
                      >
                        <path
                          d="M10.325 4.317c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756 .426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543 -.826 3.31 -2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756 -2.924 1.756 -3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065z"
                        ></path>
                        <path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"></path>
                      </svg>
                    </span>
                    <span class="nav-link-title"> 配置 </span>
                  </router-link>
<!--                  <a-->
<!--                    class="nav-link"-->
<!--                    href="#"-->
<!--                    data-bs-toggle="offcanvas"-->
<!--                    data-bs-target="#offcanvasSettings"-->
<!--                  >-->
<!--                    <span class="nav-link-icon d-md-none d-lg-inline-block">-->
<!--                      &lt;!&ndash; Download SVG icon from http://tabler.io/icons/icon/settings &ndash;&gt;-->
<!--                      <svg-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                        width="24"-->
<!--                        height="24"-->
<!--                        viewBox="0 0 24 24"-->
<!--                        fill="none"-->
<!--                        stroke="currentColor"-->
<!--                        stroke-width="2"-->
<!--                        stroke-linecap="round"-->
<!--                        stroke-linejoin="round"-->
<!--                        class="icon icon-1"-->
<!--                      >-->
<!--                        <path-->
<!--                          d="M10.325 4.317c.426 -1.756 2.924 -1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543 -.94 3.31 .826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756 .426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543 -.826 3.31 -2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756 -2.924 1.756 -3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543 .94 -3.31 -.826 -2.37 -2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756 -.426 -1.756 -2.924 0 -3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94 -1.543 .826 -3.31 2.37 -2.37c1 .608 2.296 .07 2.572 -1.065z"-->
<!--                        ></path>-->
<!--                        <path d="M9 12a3 3 0 1 0 6 0a3 3 0 0 0 -6 0"></path>-->
<!--                      </svg>-->
<!--                    </span>-->
<!--                    <span class="nav-link-title"> 配置 </span>-->
<!--                  </a>-->
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div id="app">
    <router-view />
  </div>
</template>

<style scoped></style>
