<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'PingName',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:8070/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-выключение следующей строки
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>