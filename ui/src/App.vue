<template>
  <v-app>
    <div class="chatarea">
      <transition-group tag="div" name="list">
        <div v-for="message in chat" :key="message.num">
          <div v-if="message.isUser">
            <div class="d-flex justify-end">
              <v-card
                transition="slide-x-transition"
                class="msgbox user-msg mb-4 mr-5 pa-2"
                color="blue lighten-5"
              >{{ message.message }}</v-card>
            </div>
          </div>
          <div v-else>
            <div class="d-flex justify-start">
              <div class="bot-icon-div">
                <v-img
                  src="./assets/_c_choju32_0023_s512_choju32_0023_11.png"
                  height="50px"
                  width="50px"
                  aspect-ratio="1"
                  class="bot-icon"
                ></v-img>
              </div>
              <v-card class="msgbox bot-msg ml-5 mb-4 pa-2">
                {{ message.message }}
                <v-radio-group v-model="radioGroup">
                  <v-radio
                    v-for="n in 3"
                    :key="n"
                    :label="`Radio ${n}`"
                    :value="n"
                    :disabled="true"
                  ></v-radio>
                </v-radio-group>
              </v-card>
            </div>
          </div>
        </div>
      </transition-group>
    </div>
    <v-footer fixed height="80px">
      <v-text-field
        label="入力してください..."
        required
        v-model="input"
        :disabled="clicked"
        @keyup.enter="send"
        @keypress="setCanMessageSubmit"
        ref="msgArea"
      ></v-text-field>
      <v-btn color="primary" class="ml-5" @click="send" :disabled="clicked">送信</v-btn>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    chat: [],
    input: '',
    clicked: false,
    num: 0,
    canMessageSubmit: false
  }),
  methods: {
    setCanMessageSubmit: function () {
      this.canMessageSubmit = true
    },
    send: async function () {
      if (!this.canMessageSubmit) {
        return
      }
      this.clicked = true
      this.showUserInput()
      // send message to server
      this.input = ''
      await new Promise(resolve => setTimeout(resolve, 500))
      // return server response
      this.showBotInput('得意料理はなんですか？')
      this.clicked = false
      this.canMessageSubmit = false
    },
    showUserInput: function () {
      this.chat.push({
        message: this.input,
        isUser: true,
        num: this.num++
      })
      this.$nextTick(() => {
        window.scrollTo(0, document.body.clientHeight)
      })
    },
    showBotInput: function (msg) {
      this.chat.push({
        message: msg,
        isUser: false,
        num: this.num++
      })
      this.$nextTick(() => {
        window.scrollTo(0, document.body.clientHeight)
        this.$refs.msgArea.focus()
      })
    }
  }
}
</script>

<style scoped>
.chatarea {
  margin-bottom: 120px;
  margin-top: 20px;
}
.bot-icon-div {
  border-radius: 50%;
  height: 50px;
  width: 50px;
  margin-left: 5pt;
}
.bot-icon {
  border-radius: 50%;
}
.msgbox {
  min-height: 50px;
  width: 80%;
  border-radius: 8px !important;
  position: relative;
}
.user-msg:before {
  position: absolute;
  content: "";
  top: 10px;
  left: 100%;
  border: 5px solid transparent;
  border-left: 15px solid #e3f2fd;
}
.bot-msg:before {
  position: absolute;
  content: "";
  top: 10%;
  right: 100%;
  border: 5px solid transparent;
  border-right: 15px solid white;
}
.list-enter-active,
.list-leave-active {
  transition: all 0.5s;
}
.list-enter,
.list-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
