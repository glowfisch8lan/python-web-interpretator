<template>
    <q-layout>
        <navigation-menu></navigation-menu>
        <q-page-container>
          <router-view></router-view>
        </q-page-container>
    </q-layout>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import NavigationMenu from "../components/NavigationMenu.vue";
import loadingStateMixin from "@/mixins/loadingStateMixin";

export default defineComponent({
  name: 'EntryPage',
  components: {NavigationMenu},

});
</script>