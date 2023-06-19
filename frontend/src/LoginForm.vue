<template>
    <div class="form-center">
        <h2>Вход для сотрудников</h2>
        <form @submit="handleSubmit" id="login-form" class="text-center">
            <input id="username" class="form-control shadow-none" placeholder="Логин" required v-model="form.username">
            <input id="password" class="form-control shadow-none" type="password" placeholder="Пароль" required
                v-model="form.password">
            <button id="login-btn" class="btn btn-dark" type="submit">Войти</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            form: {
                username: '',
                password: '',
            }
        }
    },
    methods: {
        async handleSubmit(event) {
            event.preventDefault()
            const params = new URLSearchParams();
            params.append('username', this.form.username);
            params.append('password', this.form.password);
            let response = await axios.post('login', params)
            localStorage.setItem('access_token', response.data['access_token'])
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('access_token')
            this.$router.push('/me/current_salary')
        }
    }
}
</script>

<style scoped>
.form-center {
    padding: 15px;
    vertical-align: middle;
    position: absolute;
    width: 400px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

#username,
#password {
    margin-bottom: 10px;
}

#login-form {
    margin-bottom: 10px;
}

#login-btn {
    width: 100%
}
</style>