import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DelComponent } from './del/del.component';
import { RestComponent } from './rest/rest.component';
import { CatgComponent } from './catg/catg.component';
import { BacketComponent } from './backet/backet.component';

@NgModule({
  declarations: [
    AppComponent,
    DelComponent,
    RestComponent,
    CatgComponent,
    BacketComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
