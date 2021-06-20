<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bulma';

@media print {

  header, footer {
    display:none;
  }

}
</style>
