<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import 'snes.css/dist/snes.min.css'
  import ResetButton from './lib/ResetButton.svelte'
  import {Question} from './lib/Question.svelte.ts'
  import QuestionDisplay from './lib/QuestionDisplay.svelte'
  let questions = [new Question()]
</script>

<main>

  <h1>convote</h1>

  {#each questions as q}
    <QuestionDisplay question={q} />
  {/each}

</main>

<style>


</style>
