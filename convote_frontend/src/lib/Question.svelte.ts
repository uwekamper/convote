export class Question {
    #text = $state("Do you have a question?")
    #answers = $state(["Yes", "No"])

    constructor(question: string, answers: string[]) {
        this.#text = question
        this.#answers = answers
    }

    get text() {
        return this.#text
    }

    set text(v) {
        this.#text = v
    }

    get answers() {
        return this.#answers
    }
    set answers(v) {
        this.#answers = v
    }
    // increment = () => {
    //    this.#count += 1
    // }
}
