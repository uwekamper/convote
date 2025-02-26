<script lang="ts">
    let {question, index} = $props()
    
    let show_editor = $state(false)
    let my_text = $state("")
    let my_answers = $state([])

    const openEditor = () => {
      my_text = $state.snapshot(question.text)  // local copy of the question text
      my_answers = $state.snapshot(question.answers)
      show_editor = true
    }
    
    const saveEditor = () => {
      question.text = $state.snapshot(my_text)
      question.answers = $state.snapshot(my_answers)
      show_editor = false
    }
    
    const discardEditor = () => {
      show_editor = false
    }

    const addAnswer = () => {
      let tmp_answers = $state.snapshot(my_answers)
      tmp_answers.push('')
      my_answers = tmp_answers
    } 
    const removeAnswer = (index: number) => {
      let tmp_answers = $state.snapshot(my_answers)
      tmp_answers.splice(index, 1)
      my_answers = tmp_answers
    } 
</script>

<div class="snes-container" style="margin-top: 40px; text-align: left; width: 50vw;">
  {#if show_editor}
  <div class="snes-form-group">
    <a id={`#question-${index}`}></a>
    <label for="input-question">Question</label>
    <div class="snes-input">
      <input id="input-question" type="text" value={my_text} onkeyup={(ev) => {my_text = ev.target.value}} placeholder="Enter a question" />
    </div>
    <label for="input-answers">Answers</label>
    {#each my_answers as answer, index }
      <div class="snes-input">
        <input id="input-question" type="text" bind:value={my_answers[index]} placeholder="Enter an answer" />
        <button class="snes-button has-plumber-color" title="Remove this question."
                onclick={() => {removeAnswer(index)}}>-</button>
      </div>
    {/each}
    <div style="width: 100%; text-align: right;">
      <button class="snes-button has-ocean-color" 
              title="Add another answer option (4 max.)" onclick={() => {addAnswer()}}
              disabled={my_answers.length > 3}>+</button>
    </div>
  </div>

  <button class="snes-button has-sunshine-color" style="margin-right: 20px;" onclick={() => saveEditor()}>Save</button>
  <button class="snes-button has-plumber-color" onclick={() => discardEditor()}>Discard</button>
  {:else}
  <h4 class="snes-container-title has-ember-underline">{question.text}</h4>
  <div class="snes-form-group">
    <label>Answers</label>
    <div class="snes-radio snes-radio--vertical has-ember-icons">
      {#each question.answers as answer, index }
      <label class="snes-radio__item">
        <input type="radio" name="class" value="warrior" checked={index == 0} />
        <span class="snes-radio__item__content">{answer}</span>
      </label>
      {:else}
      No answers defined.
      {/each}
    </div>
    
  </div>
  <div>
  <a href={`#question-${index}`} class="snes-link text-galaxy-color">Ask</a>
  <a href={`#question-${index}`} class="snes-link text-plumber-color" onclick={() => { openEditor() }}>Edit</a>
  </div>
  {/if}
</div>