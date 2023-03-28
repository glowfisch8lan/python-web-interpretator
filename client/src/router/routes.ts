import {RouteRecordRaw} from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/python-web',
    component: () => import('../pages/EntryPage.vue'),
    children: [
        {
          name:'PythonWeb',
          path: '',
          component: () => import('../pages/Main.vue')},
    ],
  },
];

export default routes;
