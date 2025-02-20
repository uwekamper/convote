<script lang="ts">
  import Counter from './lib/Counter.svelte'
  import 'snes.css/dist/snes.min.css'
  import ResetButton from './lib/ResetButton.svelte'
  import {Question} from './lib/Question.svelte.ts'
  import QuestionDisplay from './lib/QuestionDisplay.svelte'
  let questions = $state([new Question()])

  const addQuestion = () => {
    // let tmp_questions = $state.snapshot(questions)
    questions.push(new Question())
    
    // questions = tmp_questions
  }

  const removeQuestion = (index: number) => {
    // let tmp_questions = $state.snapshot(questions)
    //questions.push(new Question())
    questions.splice(index, 1);
    // questions = tmp_questions
  }
</script>

<main>

  <h1>convote</h1>

  {#each questions as q, index}
    <QuestionDisplay question={q} index={index} />
    <div style="width: 98%; text-align: right; margin-top: -60px;">
      <button class="snes-button has-plumber-color" 
              title="Add another question" onclick={() => {removeQuestion(index)}}>-</button>
    </div>
  {/each}
  
  <div style="width: 100%; text-align: right; margin-top: 50px;">
    <button class="snes-button has-ocean-color" 
            title="Add another question" onclick={() => {addQuestion()}}>+</button>
            Add question
  </div>

</main>

<style>


</style>
