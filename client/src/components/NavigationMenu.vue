<template>
  <div class="sniffer--nav">
    <q-drawer
        v-model="drawer"
        show-if-above
        :mini="miniState"
        @mouseover="miniState = false"
        @mouseout="miniState = true"
        :width="200"
        :breakpoint="500"
        bordered
        mini-to-overlay
        class="bg-grey-3"
    >
      <q-scroll-area class="fit" :horizontal-thumb-style="{ opacity: 0 }">
        <div>
          <q-list padding ref="sniffer--list-button">
            <q-item clickable v-ripple :active="isActive(item)" v-for="item in menuItems" :to="{name: item.routeName}"
                    :key="item.id">
              <q-item-section avatar>
                <q-icon :name="item.icon"/>
              </q-item-section>

              <q-item-section>
                {{ item.title }}
              </q-item-section>
            </q-item>
          </q-list>
        </div>
      </q-scroll-area>
    </q-drawer>
  </div>
</template>

<script lang="ts">
import {ref, defineComponent} from "vue";
import {MenuItemDto} from "@/dtos/MenuItemDto";

export default defineComponent({
  setup() {
    const scrollInfo = ref({})

    return {
      scrollInfo,
      onScroll(info: {}) {
        scrollInfo.value = info
      },
      drawer: ref(false),
      miniState: ref(true)
    }
  },
  created() {

  },
  mounted() {
    window.addEventListener('scroll', function(event) {

    });
    console.log(this.$refs["sniffer--list-button"]);
  },
  name: "NavigationMenu",
  data() {
    return {
      _paddingScroll: 0,
      menuItems: [
        {
          id: 1,
          title: 'Python Web',
          icon: "list",
          routeName: "PythonWeb",
          link: "/python-web",
        },
      ]
    }
  },
  computed: {
    style(): any {
      return {
        "padding-top": this._paddingScroll + 'px',
      }
    }
  },
  methods: {
    scrollHandler(details: any) {
      console.log(details)
      this._paddingScroll += 10;
    },
    isActive(item: MenuItemDto): boolean {
      return this.$route?.name === item.routeName;
    }
  }
});
</script>

<style>

.sniffer--nav aside.q-drawer {
  position: absolute !important;
  z-index: 1 !important;
}
</style>
