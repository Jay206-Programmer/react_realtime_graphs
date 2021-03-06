export default class EventStream {
  constructor(url, onMessageCallback, onOpenCallback= ()=>{}) {
    this.evtSource = new EventSource(url);

    this.evtSource.onopen = (event) => {
      console.log(`Event Stream Opened on Url: ${this.evtSource.url}`);
      onOpenCallback(event)
    };

    this.evtSource.onmessage = function (event) {
      onMessageCallback(event);
    };

    this.evtSource.onerror = function (event) {
      console.log("Something went wrong")
    }
  }

  close(){
    this.evtSource.close()
  }

  getEventSourceObject(){
    return this.evtSource
  }
}