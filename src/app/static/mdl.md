# Purpose of this page  
  
Herein lies the contents found on [MDL's documentation](https://getmdl.io/components/index.html) in the 
carniverous case of Google shutdown. They have a habit of rampant destructionism, 
and with MDL retirement being sought, the desire of this file is to immortalize, in 
a way, their own documentation.  
  
## Badges  
  
Small status descriptors for UI elements.  
  
```
<!-- Number badge on icon -->
<div class="material-icons mdl-badge mdl-badge--overlap" data-badge="1">account_box</div>

<!-- Icon badge on icon -->
<div class="material-icons mdl-badge mdl-badge--overlap" data-badge="♥">account_box</div>
```

```
<!-- Number badge -->
<span class="mdl-badge" data-badge="4">Inbox</span>

<!-- Icon badge -->
<span class="mdl-badge" data-badge="♥">Mood</span>
```
  
### Introduction  
  
The MDL CSS classes apply various predefined visual enhancements to the badge. The table below lists the available classes and their effects.  
  
| MDL class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-badge | Defines badge as an MDL component | Required on span or link |
| mdl-badge--no-background | Applies open-circle effect to badge | Optional |
| mdl-badge--overlap | Make the badge overlap with its container | Optional |
| data-badge="value" | Assigns string value to badge | Not a class, but a separate attribute; required on span or link |
  
## Buttons  
  
Variations on Material Design buttons.  
  
```
<!-- Colored FAB button -->
<button class="mdl-button mdl-js-button mdl-button--fab mdl-button--colored">
  <i class="material-icons">add</i>
</button>

<!-- Colored FAB button with ripple -->
<button class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect mdl-button--colored">
  <i class="material-icons">add</i>
</button>
```

```
<!-- FAB button -->
<button class="mdl-button mdl-js-button mdl-button--fab">
  <i class="material-icons">add</i>
</button>

<!-- FAB button with ripple -->
<button class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect">
  <i class="material-icons">add</i>
</button>

<!-- Disabled FAB button -->
<button class="mdl-button mdl-js-button mdl-button--fab" disabled>
  <i class="material-icons">add</i>
</button>
```

```
<!-- Raised button -->
<button class="mdl-button mdl-js-button mdl-button--raised">
  Button
</button>

<!-- Raised button with ripple -->
<button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect">
  Button
</button>

<!-- Raised disabled button -->
<button class="mdl-button mdl-js-button mdl-button--raised" disabled>
  Button
</button>
```

```
<!-- Colored raised button -->
<button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
  Button
</button>

<!-- Accent-colored raised button -->
<button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent">
  Button
</button>

<!-- Accent-colored raised button with ripple -->
<button class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent">
  Button
</button>
```

```
<!-- Flat button -->
<button class="mdl-button mdl-js-button">
  Button
</button>

<!-- Flat button with ripple -->
<button class="mdl-button mdl-js-button mdl-js-ripple-effect">
  Button
</button>

<!-- Disabled flat button -->
<button class="mdl-button mdl-js-button" disabled>
  Button
</button>
```

```
<!-- Primary-colored flat button -->
<button class="mdl-button mdl-js-button mdl-button--primary">
  Button
</button>

<!-- Accent-colored flat button -->
<button class="mdl-button mdl-js-button mdl-button--accent">
  Button
</button>
```

```
<!-- Icon button -->
<button class="mdl-button mdl-js-button mdl-button--icon">
  <i class="material-icons">mood</i>
</button>

<!-- Colored icon button -->
<button class="mdl-button mdl-js-button mdl-button--icon mdl-button--colored">
  <i class="material-icons">mood</i>
</button>
```

```
<!-- Mini FAB button -->
<button class="mdl-button mdl-js-button mdl-button--fab mdl-button--mini-fab">
  <i class="material-icons">add</i>
</button>

<!-- Colored mini FAB button -->
<button class="mdl-button mdl-js-button mdl-button--fab mdl-button--mini-fab mdl-button--colored">
  <i class="material-icons">add</i>
</button>
```

### Introduction

The Material Design Lite (MDL) button component is an enhanced version of the standard HTML `<button>` element. A button consists of text and/or an image that clearly communicates what action will occur when the user clicks or touches it. The MDL button component provides various types of buttons, and allows you to add both display and click effects.

Buttons are a ubiquitous feature of most user interfaces, regardless of a site's content or function. Their design and use is therefore an important factor in the overall user experience. See the button component's Material Design specifications page for details.

The available button display types are flat (default), raised, fab, mini-fab, and icon; any of these types may be plain (light gray) or colored, and may be initially or programmatically disabled. The fab, mini-fab, and icon button types typically use a small image as their caption rather than text.

| MDL class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-button | Defines button as an MDL component | Required |
| mdl-js-button | Assigns basic MDL behavior to button | Required |
| (none) | Applies flat display effect to button (default) | n/a |
| mdl-button--raised | Applies raised display effect | Mutually exclusive with fab, mini-fab, and icon |
| mdl-button--fab | Applies fab (circular) display effect | Mutually exclusive with raised, mini-fab, and icon |
| mdl-button--mini-fab | Applies mini-fab (small fab circular) display effect	| Mutually exclusive with raised, fab, and icon |
| mdl-button--icon | Applies icon (small plain circular) display effect	| Mutually exclusive with raised, fab, and mini-fab |
| mdl-button--colored | Applies colored display effect (primary or accent color, depending on the type of button) | Colors are defined in material.min.css |
| mdl-button--primary | Applies primary color display effect | Colors are defined in material.min.css |
| mdl-button--accent | Applies accent color display effect | Colors are defined in material.min.css |
| mdl-js-ripple-effect | Applies ripple click effect | May be used in combination with any other classes |


## Cards

Self-contained pieces of paper with data.

```
<!-- Wide card with share menu button -->
<style>
.demo-card-wide.mdl-card {
  width: 512px;
}
.demo-card-wide > .mdl-card__title {
  color: #fff;
  height: 176px;
  background: url('../assets/demos/welcome_card.jpg') center / cover;
}
.demo-card-wide > .mdl-card__menu {
  color: #fff;
}
</style>

<div class="demo-card-wide mdl-card mdl-shadow--2dp">
  <div class="mdl-card__title">
    <h2 class="mdl-card__title-text">Welcome</h2>
  </div>
  <div class="mdl-card__supporting-text">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Mauris sagittis pellentesque lacus eleifend lacinia...
  </div>
  <div class="mdl-card__actions mdl-card--border">
    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
      Get Started
    </a>
  </div>
  <div class="mdl-card__menu">
    <button class="mdl-button mdl-button--icon mdl-js-button mdl-js-ripple-effect">
      <i class="material-icons">share</i>
    </button>
  </div>
</div>
```

```
<!-- Square card -->
<style>
.demo-card-square.mdl-card {
  width: 320px;
  height: 320px;
}
.demo-card-square > .mdl-card__title {
  color: #fff;
  background:
    url('../assets/demos/dog.png') bottom right 15% no-repeat #46B6AC;
}
</style>

<div class="demo-card-square mdl-card mdl-shadow--2dp">
  <div class="mdl-card__title mdl-card--expand">
    <h2 class="mdl-card__title-text">Update</h2>
  </div>
  <div class="mdl-card__supporting-text">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Aenan convallis.
  </div>
  <div class="mdl-card__actions mdl-card--border">
    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
      View Updates
    </a>
  </div>
</div>
```

```
<!-- Image card -->
<style>
.demo-card-image.mdl-card {
  width: 256px;
  height: 256px;
  background: url('../assets/demos/image_card.jpg') center / cover;
}
.demo-card-image > .mdl-card__actions {
  height: 52px;
  padding: 16px;
  background: rgba(0, 0, 0, 0.2);
}
.demo-card-image__filename {
  color: #fff;
  font-size: 14px;
  font-weight: 500;
}
</style>

<div class="demo-card-image mdl-card mdl-shadow--2dp">
  <div class="mdl-card__title mdl-card--expand"></div>
  <div class="mdl-card__actions">
    <span class="demo-card-image__filename">Image.jpg</span>
  </div>
</div>

<!-- Event card -->
<style>
.demo-card-event.mdl-card {
  width: 256px;
  height: 256px;````````````
  background: #3E4EB8;
}
.demo-card-event > .mdl-card__actions {
  border-color: rgba(255, 255, 255, 0.2);
}
.demo-card-event > .mdl-card__title {
  align-items: flex-start;
}
.demo-card-event > .mdl-card__title > h4 {
  margin-top: 0;
}
.demo-card-event > .mdl-card__actions {
  display: flex;
  box-sizing:border-box;
  align-items: center;
}
.demo-card-event > .mdl-card__actions > .material-icons {
  padding-right: 10px;
}
.demo-card-event > .mdl-card__title,
.demo-card-event > .mdl-card__actions,
.demo-card-event > .mdl-card__actions > .mdl-button {
  color: #fff;
}
</style>

<div class="demo-card-event mdl-card mdl-shadow--2dp">
  <div class="mdl-card__title mdl-card--expand">
    <h4>
      Featured event:<br>
      May 24, 2016<br>
      7-11pm
    </h4>
  </div>
  <div class="mdl-card__actions mdl-card--border">
    <a class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
      Add to Calendar
    </a>
    <div class="mdl-layout-spacer"></div>
    <i class="material-icons">event</i>
  </div>
</div>
```

### Introduction

The Material Design Lite (MDL) card component is a user interface element representing a virtual piece of paper that contains related data — such as a photo, some text, and a link — that are all about a single subject.

Cards are a convenient means of coherently displaying related content that is composed of different types of objects. They are also well-suited for presenting similar objects whose size or supported actions can vary considerably, like photos with captions of variable length. Cards have a constant width and a variable height, depending on their content.

Cards are a fairly new feature in user interfaces, and allow users an access point to more complex and detailed information. Their design and use is an important factor in the overall user experience. See the card component's Material Design specifications page for details.

### Configuration Options

The MDL CSS classes apply various predefined visual and behavioral enhancements to the card. The table below lists the available classes and their effects.

| MDL class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-card | Defines div element as an MDL card container | Required on "outer" div |
| mdl-card--border | Adds a border to the card section that it's applied to | Used on the "inner" divs |
| mdl-shadow--2dp through mdl-shadow--16dp | Assigns variable shadow depths (2, 3, 4, 6, 8, or 16) to card | Optional, goes on "outer" div; if omitted, no shadow is present |
| mdl-card__title | Defines div as a card title container | Required on "inner" title div |
| mdl-card__title-text | Assigns appropriate text characteristics to card title | Required on head tag (H1 - H6) inside title div |
| mdl-card__subtitle-text | Assigns text characteristics to a card subtitle | Optional. Should be a child of the title element. |
| mdl-card__media | Defines div as a card media container | Required on "inner" media div |
| mdl-card__supporting-text | Defines div as a card body text container and assigns appropriate text characteristics to body text | Required on "inner" body text div; text goes directly inside the div with no intervening containers |
| mdl-card__actions | Defines div as a card actions container and assigns appropriate text characteristics to actions text | Required on "inner" actions div; content goes directly inside the div with no intervening containers |
| mdl-card__menu | Defines element as top right menu button | Optional. Should be a child of the mdl-card element. |

## Chips

Represents complex entities in small blocks.

```
<!-- Basic Chip -->
<span class="mdl-chip">
    <span class="mdl-chip__text">Basic Chip</span>
</span>

<!-- Deletable Chip -->
<span class="mdl-chip mdl-chip--deletable">
    <span class="mdl-chip__text">Deletable Chip</span>
    <button type="button" class="mdl-chip__action"><i class="material-icons">cancel</i></button>
</span>

<!-- Button Chip -->
<button type="button" class="mdl-chip">
    <span class="mdl-chip__text">Button Chip</span>
</button>
```

```
<!-- Contact Chip -->
<span class="mdl-chip mdl-chip--contact">
    <span class="mdl-chip__contact mdl-color--teal mdl-color-text--white">A</span>
    <span class="mdl-chip__text">Contact Chip</span>
</span>

<!-- Deletable Contact Chip -->
<span class="mdl-chip mdl-chip--contact mdl-chip--deletable">
    <img class="mdl-chip__contact" src="/templates/dashboard/images/user.jpg"></img>
    <span class="mdl-chip__text">Deletable Contact Chip</span>
    <a href="#" class="mdl-chip__action"><i class="material-icons">cancel</i></a>
</span>
```

### Introduction

The Material Design Lite (MDL) chip component is a small, interactive element. Chips are commonly used for contacts, text, rules, icons, and photos.

- Create a container element for the chip; typically `<span>` and `<div>` are used, but any container element should work equally well. If you need interactivity, use a `<button>`, or add the tabindex attribute to your container.

```
<span>
</span>
```

- Add in the text wrapper and the MDL classes.

```
<span class="mdl-chip">
    <span class="mdl-chip__text">Chip Text</span>
</span>
```

- For deletable chips, add in the delete icon. This can be an `<a>`, `<button>` or non-interactive tags like `<span>`.

```
<span class="mdl-chip">
    <span class="mdl-chip__text">Chip Text</span>
    <a href="#" class="mdl-chip__action"><i class="material-icons">cancel</i></a>
</span>
```

- Contact chips need to have the mdl-chip--contact class added to the container, along with another container for the contact icon. The icon container for photos is typically an `<img>` tag, but other types of content can be used with a little extra supporting css.

```
<span class="mdl-chip">
    <span class="mdl-chip__contact mdl-color--teal mdl-color-text--white">A</span>
    <span class="mdl-chip__text">Chip Text</span>
    <a href="#" class="mdl-chip__action"><i class="material-icons">cancel</i></a>
</span>
```

### Example

A button based contact chip whose contact image is a `<span>` with a background-image.

```
<style>
    .demo-chip .mdl-chip__contact {
        background-image: url("./path/to/image");
        background-size: cover;
    }
</style>

<button class="mdl-chip demo-chip">
    <span class="mdl-chip__contact">&nbsp;</span>
    <span class="mdl-chip__text">Chip Text</span>
    <a href="#" class="mdl-chip__action"><i class="material-icons">cancel</i></a>
</button>
```

### Configuration Options

| MDL Class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-chip | Defines element as an MDL chip container | Required on "outer" container |
| mdl-chip--contact | Defines an MDL chip as a contact style chip | Optional, goes on "outer" container |
| mdl-chip__text | Defines element as the chip's text | Required on "inner" text container |
| mdl-chip__action | Defines element as the chip's action | Required on "inner" action container, if present |
| mdl-chip__contact | Defines element as the chip's contact container | Required on "inner" contact container, if the mdl-chip--contact class is present on "outer" container |


## Dialogs

**Note:** Dialogs use the HTML <dialog> element, which currently has very limited cross-browser support. To ensure support across all modern browsers, please consider using a polyfill or creating your own. There is no polyfill included with MDL.

The Material Design Lite (MDL) dialog component allows for verification of user actions, simple data input, and alerts to provide extra information to users.

### Basic Usage

To use the dialog component, you must be using a browser that supports the dialog element. Only Chrome and Opera have native support at the time of writing. For other browsers you will need to include the dialog polyfill or create your own.

Once you have dialog support create a dialog element. The element when using the polyfill must be a child of the body element. Within that container, add a content element with the class mdl-dialog__content. Add you content, then create an action container with the class mdl-dialog__actions. Finally for the markup, add your buttons within this container for triggering dialog functions.

Keep in mind, the order is automatically reversed for actions. Material Design requires that the primary (confirmation) action be displayed last. So, the first action you create will appear last on the action bar. This allows for more natural coding and tab ordering while following the specification.

Remember to add the event handlers for your action items. After your dialog markup is created, add the event listeners to the page to trigger the dialog to show.

### Examples

#### Simple Dialog

```
<body>
  <button id="show-dialog" type="button" class="mdl-button">Show Dialog</button>
  <dialog class="mdl-dialog">
    <h4 class="mdl-dialog__title">Allow data collection?</h4>
    <div class="mdl-dialog__content">
      <p>
        Allowing us to collect data will let us get you the information you want faster.
      </p>
    </div>
    <div class="mdl-dialog__actions">
      <button type="button" class="mdl-button">Agree</button>
      <button type="button" class="mdl-button close">Disagree</button>
    </div>
  </dialog>
  <script>
    var dialog = document.querySelector('dialog');
    var showDialogButton = document.querySelector('#show-dialog');
    if (! dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    showDialogButton.addEventListener('click', function() {
      dialog.showModal();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
      dialog.close();
    });
  </script>
</body>
```

#### Dialog with full width actions

```
<body>
  <button type="button" class="mdl-button show-modal">Show Modal</button>
  <dialog class="mdl-dialog">
    <div class="mdl-dialog__content">
      <p>
        Allow this site to collect usage data to improve your experience?
      </p>
    </div>
    <div class="mdl-dialog__actions mdl-dialog__actions--full-width">
      <button type="button" class="mdl-button">Agree</button>
      <button type="button" class="mdl-button close">Disagree</button>
    </div>
  </dialog>
  <script>
    var dialog = document.querySelector('dialog');
    var showModalButton = document.querySelector('.show-modal');
    if (! dialog.showModal) {
      dialogPolyfill.registerDialog(dialog);
    }
    showModalButton.addEventListener('click', function() {
      dialog.showModal();
    });
    dialog.querySelector('.close').addEventListener('click', function() {
      dialog.close();
    });
  </script>
</body>
```

### Configuration

#### Blocks

| MDL Class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-dialog | Defines the container of the dialog component. | Required on dialog container. |

#### Elements

| MDL Class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-dialog__title | Defines the title container in the dialog. | Optional on title container. |
| mdl-dialog__content | Defines the content container of the dialog. | Required on content container. |
| mdl-dialog__actions | Defines the actions container in the dialog. | Required on action container. |

#### Modifiers

| MDL Class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-dialog__actions--full-width | Modifies the actions to each take the full width of the container. | This makes each take their own line.	Optional on action container. |


## Layout
  
Building blocks for constructing a page layout.  
  
### Navigation layouts  
  
Transparent header  
  
```
<!-- Uses a transparent header that draws on top of the layout's background -->
<style>
.demo-layout-transparent {
  background: url('../assets/demos/transparent.jpg') center / cover;
}
.demo-layout-transparent .mdl-layout__header,
.demo-layout-transparent .mdl-layout__drawer-button {
  /* This background is dark, so we set text to white. Use 87% black instead if
     your background is light. */
  color: white;
}
</style>

<div class="demo-layout-transparent mdl-layout mdl-js-layout">
  <header class="mdl-layout__header mdl-layout__header--transparent">
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">Title</span>
      <!-- Add spacer, to align navigation to the right -->
      <div class="mdl-layout-spacer"></div>
      <!-- Navigation -->
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
  </main>
</div>
```
  
Fixed drawer no header  
  
```
<!-- No header, and the drawer stays open on larger screens (fixed drawer). -->
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-drawer">
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div class="page-content"><!-- Your content goes here --></div>
  </main>
</div>
```
  
Fixed header  
  
```
<!-- Always shows a header, even in smaller screens. -->
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
  <header class="mdl-layout__header">
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">Title</span>
      <!-- Add spacer, to align navigation to the right -->
      <div class="mdl-layout-spacer"></div>
      <!-- Navigation. We hide it in small screens. -->
      <nav class="mdl-navigation mdl-layout--large-screen-only">
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div class="page-content"><!-- Your content goes here --></div>
  </main>
</div>
```
  
Fixed header and drawer  
  
```
<!-- The drawer is always open in large screens. The header is always shown,
  even in small screens. -->
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-drawer
            mdl-layout--fixed-header">
  <header class="mdl-layout__header">
    <div class="mdl-layout__header-row">
      <div class="mdl-layout-spacer"></div>
      <div class="mdl-textfield mdl-js-textfield mdl-textfield--expandable
                  mdl-textfield--floating-label mdl-textfield--align-right">
        <label class="mdl-button mdl-js-button mdl-button--icon"
               for="fixed-header-drawer-exp">
          <i class="material-icons">search</i>
        </label>
        <div class="mdl-textfield__expandable-holder">
          <input class="mdl-textfield__input" type="text" name="sample"
                 id="fixed-header-drawer-exp">
        </div>
      </div>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div class="page-content"><!-- Your content goes here --></div>
  </main>
</div>
```
  
Scrolling header  
  
```
<!-- Uses a header that scrolls with the text, rather than staying
  locked at the top -->
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header mdl-layout__header--scroll">
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">Title</span>
      <!-- Add spacer, to align navigation to the right -->
      <div class="mdl-layout-spacer"></div>
      <!-- Navigation -->
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div class="page-content"><!-- Your content goes here --></div>
  </main>
</div>
```
  
Waterfall header  
  
```
<!-- Uses a header that contracts as the page scrolls down. -->
<style>
.demo-layout-waterfall .mdl-layout__header-row .mdl-navigation__link:last-of-type  {
  padding-right: 0;
}
</style>

<div class="demo-layout-waterfall mdl-layout mdl-js-layout">
  <header class="mdl-layout__header mdl-layout__header--waterfall">
    <!-- Top row, always visible -->
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">Title</span>
      <div class="mdl-layout-spacer"></div>
      <div class="mdl-textfield mdl-js-textfield mdl-textfield--expandable
                  mdl-textfield--floating-label mdl-textfield--align-right">
        <label class="mdl-button mdl-js-button mdl-button--icon"
               for="waterfall-exp">
          <i class="material-icons">search</i>
        </label>
        <div class="mdl-textfield__expandable-holder">
          <input class="mdl-textfield__input" type="text" name="sample"
                 id="waterfall-exp">
        </div>
      </div>
    </div>
    <!-- Bottom row, not visible on scroll -->
    <div class="mdl-layout__header-row">
      <div class="mdl-layout-spacer"></div>
      <!-- Navigation -->
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
      <a class="mdl-navigation__link" href="">Link</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div class="page-content"><!-- Your content goes here --></div>
  </main>
</div>
```
  
Scrollable tabs  
  
```
<!-- Simple header with scrollable tabs. -->
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
  <header class="mdl-layout__header">
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">Title</span>
    </div>
    <!-- Tabs -->
    <div class="mdl-layout__tab-bar mdl-js-ripple-effect">
      <a href="#scroll-tab-1" class="mdl-layout__tab is-active">Tab 1</a>
      <a href="#scroll-tab-2" class="mdl-layout__tab">Tab 2</a>
      <a href="#scroll-tab-3" class="mdl-layout__tab">Tab 3</a>
      <a href="#scroll-tab-4" class="mdl-layout__tab">Tab 4</a>
      <a href="#scroll-tab-5" class="mdl-layout__tab">Tab 5</a>
      <a href="#scroll-tab-6" class="mdl-layout__tab">Tab 6</a>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
  </div>
  <main class="mdl-layout__content">
    <section class="mdl-layout__tab-panel is-active" id="scroll-tab-1">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-2">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-3">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-4">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-5">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="scroll-tab-6">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
  </main>
</div>
```
  
Fixed tabs  
  
```
<!-- Simple header with fixed tabs. -->
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-header
            mdl-layout--fixed-tabs">
  <header class="mdl-layout__header">
    <div class="mdl-layout__header-row">
      <!-- Title -->
      <span class="mdl-layout-title">Title</span>
    </div>
    <!-- Tabs -->
    <div class="mdl-layout__tab-bar mdl-js-ripple-effect">
      <a href="#fixed-tab-1" class="mdl-layout__tab is-active">Tab 1</a>
      <a href="#fixed-tab-2" class="mdl-layout__tab">Tab 2</a>
      <a href="#fixed-tab-3" class="mdl-layout__tab">Tab 3</a>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout-title">Title</span>
  </div>
  <main class="mdl-layout__content">
    <section class="mdl-layout__tab-panel is-active" id="fixed-tab-1">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="fixed-tab-2">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
    <section class="mdl-layout__tab-panel" id="fixed-tab-3">
      <div class="page-content"><!-- Your content goes here --></div>
    </section>
  </main>
</div>
```
  
#### Introduction
  
The Material Design Lite (MDL) layout component is a comprehensive approach to page layout that uses MDL development tenets, allows for efficient use of MDL components, and automatically adapts to different browsers, screen sizes, and devices.
  
Appropriate and accessible layout is a critical feature of all user interfaces, regardless of a site's content or function. Page design and presentation is therefore an important factor in the overall user experience. See the layout component's [Material Design specifications page](http://www.google.com/design/spec/layout/principles.html) for details.
  
Use of MDL layout principles simplifies the creation of scalable pages by providing reusable components and encourages consistency across environments by establishing recognizable visual elements, adhering to logical structural grids, and maintaining appropriate spacing across multiple platforms and screen sizes. MDL layout is extremely powerful and dynamic, allowing for great consistency in outward appearance and behavior while maintaining development flexibility and ease of use.  
  
#### To include a basic MDL layout component:  
  
1. Code a `<div>` element. This is the "outer" div that holds the entire layout.

```
<div>
</div>
```
  
***Note:** The layout cannot be applied directly on the `<body>` element. Always create a nested `<div>` element.*
  
2. Add MDL classes as indicated, separated by spaces, to the div using the `class` attribute.
  
```
<div class="mdl-layout mdl-js-layout">
</div>
```
  
3. Inside the div, code a `<header>` element. This holds the header row with navigation links that is displayed on large screens, and the menu icon that opens the navigation drawer for smaller screens. Add the MDL class to the header using the `class` attribute.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
  </header>
</div>
```
  
4. Inside the header, add a `<div>` to produce the menu icon, and include the MDL class as indicated. The div has no content of its own.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
  </header>
</div>
```
  
5. Still inside the header, add another `<div>` to hold the header row's content, and include the MDL class as indicated.

```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
    </div>
  </header>
</div>
```
  
6. Inside the header row div, add a span containing the layout title, and include the MDL class as indicated.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Simple Layout</span>
    </div>
  </header>
</div>
```
  
7. Following the span, add a `<div>` to align the header's navigation links to the right, and include the MDL class as indicated.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Simple Layout</span>
      <div class="mdl-layout-spacer"></div>
    </div>
  </header>
</div>
```
  
8. Following the spacer div, add a `<nav>` element to contain the header's navigation links, and include the MDL class as indicated. Inside the nav, add one anchor `<a>` element for each header link, and include the MDL class as indicated. This completes the layout's header.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Simple Layout</span>
      <div class="mdl-layout-spacer"></div>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="#">Nav link 1</a>
        <a class="mdl-navigation__link" href="#">Nav link 2</a>
        <a class="mdl-navigation__link" href="#">Nav link 3</a>
      </nav>
    </div>
  </header>
</div>
```
  
9. Following the header, add a `<div>` element to hold the slide-out drawer's content, and add the MDL class as indicated. The drawer appears automatically on smaller screens, and may be opened with the menu icon on any screen size.  
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Simple Layout</span>
      <div class="mdl-layout-spacer"></div>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="#">Nav link 1</a>
        <a class="mdl-navigation__link" href="#">Nav link 2</a>
        <a class="mdl-navigation__link" href="#">Nav link 3</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
  </div>
</div>
```
  
10. Inside the drawer div, add a span containing the layout title (this should match the title in step 5), and include the MDL class as indicated.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Simple Layout</span>
      <div class="mdl-layout-spacer"></div>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="#">Nav link 1</a>
        <a class="mdl-navigation__link" href="#">Nav link 2</a>
        <a class="mdl-navigation__link" href="#">Nav link 3</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout__title">Simple Layout</span>
  </div>
</div>
```
  
11. Following the span, add a `<nav>` element to contain the drawer's navigation links, and one anchor `<a>` element for each drawer link (these should match the links in step 7), and include the MDL classes as indicated. This completes the layout's drawer.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Simple Layout</span>
      <div class="mdl-layout-spacer"></div>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="#">Nav link 1</a>
        <a class="mdl-navigation__link" href="#">Nav link 2</a>
        <a class="mdl-navigation__link" href="#">Nav link 3</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout__title">Simple Layout</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="#">Nav link 1</a>
      <a class="mdl-navigation__link" href="#">Nav link 2</a>
      <a class="mdl-navigation__link" href="#">Nav link 3</a>
    </nav>
  </div>
</div>
```

12. Finally, following the drawer div, add a `<main>` element to hold the layout's primary content, and include the MDL class as indicated. Inside that element, add your desired content.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Simple Layout</span>
      <div class="mdl-layout-spacer"></div>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="#">Nav link 1</a>
        <a class="mdl-navigation__link" href="#">Nav link 2</a>
        <a class="mdl-navigation__link" href="#">Nav link 3</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout__title">Simple Layout</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="#">Nav link 1</a>
      <a class="mdl-navigation__link" href="#">Nav link 2</a>
      <a class="mdl-navigation__link" href="#">Nav link 3</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <p>Content</p>
    <p>Goes</p>
    <p>Here</p>
  </main>
</div>
```
  
The layout component is ready for use.
  
#### Examples
  
A layout with a fixed header for larger screens and a collapsible drawer for smaller screens.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header">
    <div class="mdl-layout-icon"></div>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Material Design Lite</span>
      <div class="mdl-layout-spacer"></div>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="#">Hello</a>
        <a class="mdl-navigation__link" href="#">World.</a>
        <a class="mdl-navigation__link" href="#">How</a>
        <a class="mdl-navigation__link" href="#">Are</a>
        <a class="mdl-navigation__link" href="#">You?</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout__title">Material Design Lite</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="#">Hello</a>
      <a class="mdl-navigation__link" href="#">World.</a>
      <a class="mdl-navigation__link" href="#">How</a>
      <a class="mdl-navigation__link" href="#">Are</a>
      <a class="mdl-navigation__link" href="#">You?</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div>Content</div>
  </main>
</div>
```
  
The same layout with a non-fixed header that scrolls with the content.
  
```
<div class="mdl-layout mdl-js-layout">
  <header class="mdl-layout__header mdl-layout__header--scroll">
    <img class="mdl-layout-icon"></img>
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Material Design Lite</span>
      <div class="mdl-layout-spacer"></div>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="#">Hello</a>
        <a class="mdl-navigation__link" href="#">World.</a>
        <a class="mdl-navigation__link" href="#">How</a>
        <a class="mdl-navigation__link" href="#">Are</a>
        <a class="mdl-navigation__link" href="#">You?</a>
      </nav>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout__title">Material Design Lite</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="#">Hello</a>
      <a class="mdl-navigation__link" href="#">World.</a>
      <a class="mdl-navigation__link" href="#">How</a>
      <a class="mdl-navigation__link" href="#">Are</a>
      <a class="mdl-navigation__link" href="#">You?</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div>Content</div>
  </main>
</div>
```
  
A layout with a fixed drawer that serves as sidebar navigation on larger screens. The drawer collapses and the menu icon is displayed on smaller screens.
  
```
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-drawer">
  <header class="mdl-layout__header">
    <div class="mdl-layout__header-row">
      <span class="mdl-layout__title">Fixed drawer layout demo</span>
    </div>
  </header>
  <div class="mdl-layout__drawer">
    <span class="mdl-layout__title">Material Design Lite</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="#">Hello</a>
      <a class="mdl-navigation__link" href="#">World.</a>
      <a class="mdl-navigation__link" href="#">How</a>
      <a class="mdl-navigation__link" href="#">Are</a>
      <a class="mdl-navigation__link" href="#">You?</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div>Content</div>
  </main>
</div>
```
  
A layout with a fixed drawer but no header.
  
```
<div class="mdl-layout mdl-js-layout mdl-layout--fixed-drawer">
  <div class="mdl-layout__drawer">
    <span class="mdl-layout__title">Material Design Lite</span>
    <nav class="mdl-navigation">
      <a class="mdl-navigation__link" href="#">Hello</a>
      <a class="mdl-navigation__link" href="#">World.</a>
      <a class="mdl-navigation__link" href="#">How</a>
      <a class="mdl-navigation__link" href="#">Are</a>
      <a class="mdl-navigation__link" href="#">You?</a>
    </nav>
  </div>
  <main class="mdl-layout__content">
    <div>Content</div>
  </main>
</div>
```
  
#### Configuration Options
  
The MDL CSS classes apply various predefined visual and behavioral enhancements to the layout. The table below lists the available classes and their effects.
  

| MDL class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-layout | Defines container as an MDL component | Required on outer div element |
| mdl-js-layout | Assigns basic MDL behavior to layout | Required on outer div element |
| mdl-layout__header | Defines container as an MDL component | Required on header element |
| mdl-layout-icon | Used for adding an application icon. Gets concealed by menu icon if both are visible. | Goes on optional icon element |
| mdl-layout__header-row | Defines container as MDL header row | Required on header content div |
| mdl-layout__title | Defines layout title text | Required on layout title span |
| mdl-layout-spacer | Used to align elements inside a header or drawer, by growing to fill remaining space. Commonly used for aligning elements to the right. | Goes on optional div following layout title |
| mdl-navigation | Defines container as MDL navigation group | Required on nav element |
| mdl-navigation__link | Defines anchor as MDL navigation link | Required on header and/or drawer anchor elements |
| mdl-layout__drawer | Defines container as MDL layout drawer | Required on drawer div element |
| mdl-layout__content | Defines container as MDL layout content | Required on main element |
| mdl-layout__header--scroll | Makes the header scroll with the content | Optional; goes on header element |
| mdl-layout--fixed-drawer | Makes the drawer always visible and open in larger screens | Optional; goes on outer div element (not drawer div element) |
| mdl-layout--fixed-header | Makes the header always visible, even in small screens | Optional; goes on outer div element |
| mdl-layout--no-drawer-button | Does not display a drawer button | Optional; goes on mdl-layout element |
| mdl-layout--no-desktop-drawer-button | Does not display a drawer button in desktop mode	| Optional; goes on mdl-layout element |
| mdl-layout--large-screen-only | Hides an element on smaller screens	| Optional; goes on any descendant of mdl-layout |
| mdl-layout--small-screen-only | Hides an element on larger screens | Optional; goes on any descendant of mdl-layout |
| mdl-layout__header--waterfall | Allows a "waterfall" effect with multiple header lines | Optional; goes on header element |
| mdl-layout__header--waterfall-hide-top | Hides the top rather than the bottom rows on a waterfall header | Optional; goes on header element. Requires mdl-layout__header--waterfall |
| mdl-layout__header--transparent | Makes header transparent (draws on top of layout background) | Optional; goes on header element |
| mdl-layout__header--seamed | Uses a header without a shadow | Optional; goes on header element |
| mdl-layout__tab-bar | Defines container as an MDL tab bar | Required on div element inside header (tabbed layout) |
| mdl-layout__tab | Defines anchor as MDL tab link | Required on tab bar anchor elements |
| is-active | Defines tab as default active tab | Optional; goes on tab bar anchor element and associated tab section element |
| mdl-layout__tab-panel | Defines container as tab content panel | Required on tab section elements |
| mdl-layout__tab-manual-switch | Disables tab switching when clicking on tab separators. Useful for disabling default behavior and setting up your own event listeners. | Optional; goes on tab bar element |
| mdl-layout--fixed-tabs | Uses fixed tabs instead of the default scrollable tabs | Optional; goes on outer div element (not div inside header) |
  
### Grid  

Responsive grid
  
```
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
  <div class="mdl-cell mdl-cell--1-col">1</div>
</div>
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--4-col">4</div>
  <div class="mdl-cell mdl-cell--4-col">4</div>
  <div class="mdl-cell mdl-cell--4-col">4</div>
</div>
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--6-col">6</div>
  <div class="mdl-cell mdl-cell--4-col">4</div>
  <div class="mdl-cell mdl-cell--2-col">2</div>
</div>
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--6-col mdl-cell--8-col-tablet">6 (8 tablet)</div>
  <div class="mdl-cell mdl-cell--4-col mdl-cell--6-col-tablet">4 (6 tablet)</div>
  <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-phone">2 (4 phone)</div>
</div>
```

#### Introduction

The Material Design Lite (MDL) **grid** component is a simplified method for laying out content for multiple screen sizes. It reduces the usual coding burden required to correctly display blocks of content in a variety of display conditions.

The MDL grid is defined and enclosed by a container element. A grid has 12 columns in the desktop screen size, 8 in the tablet size, and 4 in the phone size, each size having predefined margins and gutters. Cells are laid out sequentially in a row, in the order they are defined, with some exceptions:

```
If a cell doesn't fit in the row in one of the screen sizes, it flows into the following line.
If a cell has a specified column size equal to or larger than the number of columns for the current screen size, it takes up the entirety of its row.
```

You can set a maximum grid width, after which the grid stays centered with padding on either side, by setting its `max-width` CSS property.

Grids are a fairly new and non-standardized feature in most user interfaces, and provide users with a way to view content in an organized manner that might otherwise be difficult to understand or retain. Their design and use is an important factor in the overall user experience.

#### To include and MDL grid component:
  
1. Code a `<div>` element; this is the "outer" container, intended to hold all of the grid's cells. Style the div as desired (colors, font size, etc.).
  
```
<div>
</div>
```
  
2. Add the `mdl-grid` MDL class to the div using the `class` attribute.
  
```
<div class="mdl-grid">
</div>
```
  
3. For each cell, code one "inner" div, including the text to be displayed.
  
```
<div class="mdl-grid">
  <div>Content</div>
  <div>goes</div>
  <div>here</div>
</div>
```
  
4. Add the `mdl-cell` class and an `mdl-cell--COLUMN-col` class, where COLUMN specifies the column size for the cell, to the "inner" divs using the `class` attribute.
  
```
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--4-col">Content</div>
  <div class="mdl-cell mdl-cell--4-col">goes</div>
  <div class="mdl-cell mdl-cell--4-col">here</div>
</div>
```
  
5. Optionally add an `mdl-cell--COLUMN-col-DEVICE` class, where COLUMN specifies the column size for the cell on a specific device, and DEVICE specifies the device type.
  
```
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--4-col mdl-cell--8-col-tablet">Content</div>
  <div class="mdl-cell mdl-cell--4-col mdl-cell--8-col-tablet">goes</div>
  <div class="mdl-cell mdl-cell--4-col mdl-cell--8-col-tablet">here</div>
</div>
```
  
The grid component is ready for use.
  
#### Examples
  
A grid with five cells of column size 1.
  
```
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--1-col">CS 1</div>
  <div class="mdl-cell mdl-cell--1-col">CS 1</div>
  <div class="mdl-cell mdl-cell--1-col">CS 1</div>
  <div class="mdl-cell mdl-cell--1-col">CS 1</div>
  <div class="mdl-cell mdl-cell--1-col">CS 1</div>
</div>
```
  
A grid with three cells, one of column size 6, one of column size 4, and one of column size 2.
  
```
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--6-col">CS 6</div>
  <div class="mdl-cell mdl-cell--4-col">CS 4</div>
  <div class="mdl-cell mdl-cell--2-col">CS 2</div>
</div>
```
  
A grid with three cells of column size 6 that will display as column size 8 on a tablet device.
  
```
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--6-col mdl-cell--8-col-tablet">CS 6 (8 on tablet)</div>
  <div class="mdl-cell mdl-cell--6-col mdl-cell--8-col-tablet">CS 6 (8 on tablet)</div>
  <div class="mdl-cell mdl-cell--6-col mdl-cell--8-col-tablet">CS 6 (8 on tablet)</div>
</div>
```
  
A grid with four cells of column size 2 that will display as column size 4 on a phone device.
  
```
<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-phone">CS 2 (4 on phone)</div>
  <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-phone">CS 2 (4 on phone)</div>
  <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-phone">CS 2 (4 on phone)</div>
  <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-phone">CS 2 (4 on phone)</div>
</div>
```
  
#### Configuration Options
  
The MDL CSS classes apply various predefined visual enhancements and behavioral effects to the grid. The table below lists the available classes and their effects.
  
| MDL class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-grid | Defines a container as an MDL grid component | Required on "outer" div element |
| mdl-cell | Defines a container as an MDL cell | Required on "inner" div elements |
| mdl-grid--no-spacing | Modifies the grid cells to have no margin between them. | Optional on grid container. |
| mdl-cell--N-col | Sets the column size for the cell to N | N is 1-12 inclusive, defaults to 4; optional on "inner" div elements |
| mdl-cell--N-col-desktop | Sets the column size for the cell to N in desktop mode only | N is 1-12 inclusive; optional on "inner" div elements |
| mdl-cell--N-col-tablet | Sets the column size for the cell to N in tablet mode only | N is 1-8 inclusive; optional on "inner" div elements |
| mdl-cell--N-col-phone | Sets the column size for the cell to N in phone mode only | N is 1-4 inclusive; optional on "inner" div elements |
| mdl-cell--N-offset | Adds N columns of whitespace before the cell | N is 1-11 inclusive; optional on "inner" div elements |
| mdl-cell--N-offset-desktop | Adds N columns of whitespace before the cell in desktop mode | N is 1-11 inclusive; optional on "inner" div elements |
| mdl-cell--N-offset-tablet | Adds N columns of whitespace before the cell in tablet mode | N is 1-7 inclusive; optional on "inner" div elements |
| mdl-cell--N-offset-phone | Adds N columns of whitespace before the cell in phone mode | N is 1-3 inclusive; optional on "inner" div elements |
| mdl-cell--order-N | Reorders cell to position N	| N is 1-12 inclusive; optional on "inner" div elements |
| mdl-cell--order-N-desktop | Reorders cell to position N when in desktop mode | N is 1-12 inclusive; optional on "inner" div elements |
| mdl-cell--order-N-tablet | Reorders cell to position N when in tablet mode | N is 1-12 inclusive; optional on "inner" div elements |
| mdl-cell--order-N-phone | Reorders cell to position N when in phone mode | N is 1-12 inclusive; optional on "inner" div elements |
| mdl-cell--hide-desktop | Hides the cell when in desktop mode | Optional on "inner" div elements |
| mdl-cell--hide-tablet | Hides the cell when in tablet mode | Optional on "inner" div elements |
| mdl-cell--hide-phone | Hides the cell when in phone mode | Optional on "inner" div elements |
| mdl-cell--stretch | Stretches the cell vertically to fill the parent | Default; optional on "inner" div elements |
| mdl-cell--top | Aligns the cell to the top of the parent | Optional on "inner" div elements |
| mdl-cell--middle | Aligns the cell to the middle of the parent | Optional on "inner" div elements |
| mdl-cell--bottom | Aligns the cell to the bottom of the parent | Optional on "inner" div elements |
  
#### Tabs
  
Content tabs
  
```
<div class="mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
  <div class="mdl-tabs__tab-bar">
      <a href="#starks-panel" class="mdl-tabs__tab is-active">Starks</a>
      <a href="#lannisters-panel" class="mdl-tabs__tab">Lannisters</a>
      <a href="#targaryens-panel" class="mdl-tabs__tab">Targaryens</a>
  </div>

  <div class="mdl-tabs__panel is-active" id="starks-panel">
    <ul>
      <li>Eddard</li>
      <li>Catelyn</li>
      <li>Robb</li>
      <li>Sansa</li>
      <li>Brandon</li>
      <li>Arya</li>
      <li>Rickon</li>
    </ul>
  </div>
  <div class="mdl-tabs__panel" id="lannisters-panel">
    <ul>
      <li>Tywin</li>
      <li>Cersei</li>
      <li>Jamie</li>
      <li>Tyrion</li>
    </ul>
  </div>
  <div class="mdl-tabs__panel" id="targaryens-panel">
    <ul>
      <li>Viserys</li>
      <li>Daenerys</li>
    </ul>
  </div>
</div>
```
  
#### Introduction
  
The Material Design Lite (MDL) **tab** component is a user interface element that allows different content blocks to share the same screen space in a mutually exclusive manner. Tabs are always presented in sets of two or more, and they make it easy to explore and switch among different views or functional aspects of an app, or to browse categorized data sets individually. Tabs serve as "headings" for their respective content; the active tab — the one whose content is currently displayed — is always visually distinguished from the others so the user knows which heading the current content belongs to.

Tabs are an established but non-standardized feature in user interfaces, and allow users to view different, but often related, blocks of content (often called panels). Tabs save screen real estate and provide intuitive and logical access to data while reducing navigation and associated user confusion. Their design and use is an important factor in the overall user experience. See the tab component's [Material Design specifications page](http://www.google.com/design/spec/components/tabs.html) for details.
  
#### To include a set of MDL **tab** components:
  
1. Code a `<div>` element; this is the "outer" div, intended to contain all of the tabs and their content.
  
```
<div>
</div>
```
  
2. Inside the "outer" div, code one "inner" div for the tabs themselves, and one for each tab's content, all siblings. That is, for three content tabs, you would code four "inner" divs.
  
```
<div>
  <div>
  ...
  </div>
  <div>
  ...
  </div>
  <div>
  ...
  </div>
  <div>
  ...
  </div>
</div>
```
  
3.  Inside the first "inner" div (the tabs), code one anchor `<a>` (link) tag for each tab. Include `href` attributes with values to match the tabs' `id` attribute values, and some brief link text. On the remaining "inner" divs (the content), code `id` attributes whose values match the links' `hrefs`.
  
```
<div>
  <div>
    <a href="#tab1">Tab One</a>
    <a href="#tab2">Tab Two</a>
    <a href="#tab3">Tab Three</a>
  </div>
  <div id="tab1">
  ...
  </div>
  <div id="tab2">
  ...
  </div>
  <div id="tab3">
  ...
  </div>
</div>
```
  
4. Inside the remaining "inner" divs, code the content you intend to display in each panel; use standard HTML tags to structure the content as desired.
  
```
<div>
  <div>
    <a href="#tab1">Tab One</a>
    <a href="#tab2">Tab Two</a>
    <a href="#tab3">Tab Three</a>
  </div>
  <div id="tab1">
    <p>First tab's content.</p>
  </div>
  <div id="tab2">
    <p>Second tab's content.</p>
  </div>
  <div id="tab3">
    <p>Third tab's content.</p>
  </div>
</div>
```
  
5. Add one or more MDL classes, separated by spaces, to the "outer" and "inner" divs using the `class` attribute; be sure to include the `is-active` class on the tab you want to be displayed by default.
  
```
<div class="mdl-tabs mdl-js-tabs">
  <div class="mdl-tabs__tab-bar">
    <a href="#tab1" class="mdl-tabs__tab">Tab One</a>
    <a href="#tab2" class="mdl-tabs__tab">Tab Two</a>
    <a href="#tab3" class="mdl-tabs__tab">Tab Three</a>
  </div>
  <div class="mdl-tabs__panel is-active" id="tab1">
    <p>First tab's content.</p>
  </div>
  <div class="mdl-tabs__panel" id="tab2">
    <p>Second tab's content.</p>
  </div>
  <div class="mdl-tabs__panel" id="tab3">
    <p>Third tab's content.</p>
  </div>
</div>
```
  
The tab components are ready for use.
  
#### Example
  
Three tabs, with ripple effect on tab links.
  
```
<div class="mdl-tabs mdl-js-tabs mdl-js-ripple-effect">
  <div class="mdl-tabs__tab-bar">
    <a href="#about-panel" class="mdl-tabs__tab is-active">About the Beatles</a>
    <a href="#members-panel" class="mdl-tabs__tab">Members</a>
    <a href="#albums-panel" class="mdl-tabs__tab">Discography</a>
  </div>
  <div class="mdl-tabs__panel is-active" id="about-panel">
    <p><b>The Beatles</b> were a four-piece musical group from Liverpool, England.
    Formed in 1960, their career spanned just over a decade, yet they are widely
    regarded as the most influential band in history.</p>
    <p>Their songs are among the best-loved music of all time. It is said that every
    minute of every day, a radio station somewhere is playing a Beatles song.</p>
  </div>
  <div class="mdl-tabs__panel" id="members-panel">
    <p>The Beatles' members were:</p>
    <ul>
      <li>John Lennon (1940-1980)</li>
      <li>Paul McCartney (1942-)</li>
      <li>George Harrison (1943-2001)</li>
      <li>Ringo Starr (1940-)</li>
    </ul>
  </div>
  <div class="mdl-tabs__panel" id="albums-panel">
    <p>The Beatles' original UK LPs, in order of release:</p>
    <ol>
      <li>Please Please Me (1963)</li>
      <li>With the Beatles (1963)</li>
      <li>A Hard Day's Night (1964)</li>
      <li>Beatles for Sale (1964)</li>
      <li>Help! (1965)</li>
      <li>Rubber Soul (1965)</li>
      <li>Revolver (1966)</li>
      <li>Sgt. Pepper's Lonely Hearts Club Band (1967)</li>
      <li>The Beatles ("The White Album", 1968)</li>
      <li>Yellow Submarine (1969)</li>
      <li>Abbey Road (1969)</li>
      <li>Let It Be (1970)</li>
    </ol>
  </div>
</div>
```
  
#### Configuration Options
  
The MDL CSS classes apply various predefined visual and behavioral enhancements to the tabs. The table below lists the available classes and their effects.
  
| MDL class | Effect | Remarks |
|---------- |------- |-------- |
| mdl-tabs | Defines a tabs container as an MDL component | Required on "outer" div element |
| mdl-js-tabs | Assigns basic MDL behavior to tabs container | Required on "outer" div element |
| mdl-js-ripple-effect | Applies ripple click effect to tab links | Optional; goes on "outer" div element |
| mdl-tabs__tab-bar | Defines a container as an MDL tabs link bar | Required on first "inner" div element |
| mdl-tabs__tab | Defines an anchor (link) as an MDL tab activator | Required on all links in first "inner" div element |
| is-active | Defines a tab as the default display tab | Required on one (and only one) of the "inner" div (tab) elements |
| mdl-tabs__panel | Defines a container as tab content | Required on each of the "inner" div (tab) elements |




## Lists

TBD

## Loading

TBD

## Menus

TBD

## Sliders

TBD

## Snackbar

TBD

## Toggles

TBD

## Tables

TBD

## Text fields

TBD

## Tool tips

TBD
