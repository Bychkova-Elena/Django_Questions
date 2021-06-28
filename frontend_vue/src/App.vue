<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
section {
  min-height:calc(100vh - 256px);
}
@import '../node_modules/bulma';

@media print {

  header, footer {
    display:none;
  }

}
</style>
